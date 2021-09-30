from itertools import chain
from operator import attrgetter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.contrib.auth.models import User
from flux.models import Ticket, Review
from flux.forms import ReviewForm, TicketForm


@login_required
def posts(request):
    user_obj = User.objects.get(username=request.user)
    user_tickets = Ticket.objects.filter(user__exact=user_obj)
    tickets_and_reviews = user_tickets.annotate(review_user=F('review__user__username'),
                                                headline=F('review__headline'),
                                                body=F('review__body'),
                                                rating=F('review__rating'),
                                                time=F('review__time_created')
                                                ).order_by('-time_created')
    user_reviews = Ticket.objects.exclude(user__exact=user_obj).filter(review__user__exact=user_obj)
    user_reviews.annotate(review_user=F('review__user__username'),
                          headline=F('review__headline'),
                          body=F('review__body'),
                          rating=F('review__rating'),
                          time=F('review__time_created')
                          ).order_by('-time_created')
    total_posts = list(chain(tickets_and_reviews, user_reviews))
    ordered_total_posts = sorted(total_posts, key=attrgetter('time_created'), reverse=True)
    paginator = Paginator(ordered_total_posts, 5)
    page = request.GET.get('page')
    try:
        tickets = paginator.page(page)
    except PageNotAnInteger:
        tickets = paginator.page(1)
    except EmptyPage:
        tickets = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        if 'suppress' in request.POST:
            supress_id = request.POST.get("suppress")
            ticket_to_supress = Ticket.objects.get(id=supress_id)
            if ticket_to_supress.user == request.user:
                ticket_to_supress.delete()
            else:
                review_to_suppress = Review.objects.get(ticket__id=supress_id)
                review_to_suppress.delete()
            return redirect("posts")

    context = {
        'user_tickets': user_tickets,
        'tickets_and_review': tickets_and_reviews,
        'user_reviews': user_reviews,
        'total_posts': total_posts,
        'ordered_total_posts': ordered_total_posts, #utiliser ticket ou ordered_total_posts pour l'affichage dans le template?
        'tickets': tickets,
        'paginate': True,
        'user': request.user,
    }
    return render(request, 'posts/posts.html', context)


@login_required
def modify(request, ticket_number):
    user_obj = User.objects.get(username=request.user)
    ticket = Ticket.objects.filter(id=ticket_number).annotate(review_user=F('review__user__username'),
                                                              headline=F('review__headline'),
                                                              body=F('review__body'),
                                                              rating=F('review__rating'),
                                                              time=F('review__time_created')).get()

    ticket_form = TicketForm(instance=ticket)
    review_form = None
    associated_review = None

    try:
        associated_review = Review.objects.get(ticket__id=ticket_number)
        review_form = ReviewForm(instance=associated_review)
        if ticket.user == user_obj and associated_review.user == user_obj:
            if request.method == 'POST':
                ticket_form = TicketForm(request.POST, request.FILES)
                review_form = ReviewForm(request.POST)
                if ticket_form.is_valid():
                    ticket.title = ticket_form.cleaned_data.get('title')
                    ticket.description = ticket_form.cleaned_data.get('description')
                    if ticket_form.cleaned_data.get('picture') is not None:
                        ticket.picture = ticket_form.cleaned_data.get('picture')
                    ticket.save()
                if review_form.is_valid():
                    associated_review.headline = review_form.cleaned_data.get('headline')
                    associated_review.body = review_form.cleaned_data.get('body')
                    associated_review.rating = request.POST.get("ratingValue")
                    associated_review.save()
                return redirect("posts")

        elif ticket.user == user_obj and associated_review.user != user_obj:
            if request.method == 'POST':
                ticket_form = TicketForm(request.POST, request.FILES)
                ticket = Ticket.objects.get(id=ticket_number)
                if ticket_form.is_valid():
                    ticket.title = ticket_form.cleaned_data.get('title')
                    ticket.description = ticket_form.cleaned_data.get('description')
                    if ticket_form.cleaned_data.get('picture') is not None:
                        ticket.picture = ticket_form.cleaned_data.get('picture')
                    ticket.save()
                    return redirect("posts")

        elif ticket.user != user_obj and associated_review.user == user_obj:

            if request.method == 'POST':
                review_form = ReviewForm(request.POST)
                ticket = Ticket.objects.get(id=ticket_number)
                if review_form.is_valid():
                    associated_review.headline = review_form.cleaned_data.get('headline')
                    associated_review.body = review_form.cleaned_data.get('body')
                    associated_review.rating = request.POST.get("ratingValue")
                    associated_review.save()
                    return redirect("posts")

    except ObjectDoesNotExist:
        if request.method == 'POST':
            ticket_form = TicketForm(request.POST, request.FILES)
            ticket = Ticket.objects.get(id=ticket_number)
            if ticket_form.is_valid():
                ticket.title = ticket_form.cleaned_data.get('title')
                ticket.description = ticket_form.cleaned_data.get('description')
                if ticket_form.cleaned_data.get('picture') is not None:
                    ticket.picture = ticket_form.cleaned_data.get('picture')
                ticket.save()
                return redirect("posts")

    context = {
        'user_obj': user_obj,
        'ticket_form': ticket_form,
        'review_form': review_form,
        'associated_review': associated_review,
        'ticket': ticket,
    }
    return render(request, 'posts/modify.html', context)
