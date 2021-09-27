import time

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import F
from django.contrib.auth.models import User


from .models import Review, Ticket
from .forms import ReviewForm, TicketForm
from follow.models import Follow


@login_required
def flux(request):
    followed_users = Follow.objects.filter(user=request.user)
    followed_usernames = []
    for user in followed_users:
        followed_usernames.append(user.followed_user.id)
        followed_usernames.append(request.user)
    ticket_list = Ticket.objects.filter(user__in=followed_usernames).annotate(review_user=F('review__user__username'),
                                                                        headline=F('review__headline'),
                                                                        body=F('review__body'),
                                                                        rating=F('review__rating'),
                                                                        time=F('review__time_created')
                                                                        ).order_by('-time_created')
    paginator = Paginator(ticket_list, 5)
    page = request.GET.get('page')
    try:
        tickets = paginator.page(page)
    except PageNotAnInteger:
        tickets = paginator.page(1)
    except EmptyPage:
        tickets = paginator.page(paginator.num_pages)
    context = {
        'tickets':tickets,
        'paginate':True,
        'user': request.user,
        'followed_users': followed_users,
    }
    return render(request, 'flux/flux.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('home')

@login_required
def create_review(request):
    ticket_form = TicketForm(request.POST, request.FILES)
    review_form = ReviewForm(request.POST)
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        if ticket_form.is_valid():
            new_ticket = Ticket.objects.create(
                user = User.objects.get(pk=request.user.id),
                title = ticket_form.cleaned_data.get('title'),
                description = ticket_form.cleaned_data.get('description'),
                picture = ticket_form.cleaned_data.get('picture'),
            )
            new_ticket.save()
        if review_form.is_valid():
            linked_ticket = Ticket.objects.filter(user__exact = request.user).order_by('-time_created')[0]
            new_review = Review.objects.create(
                user = User.objects.get(pk=request.user.id),
                rating = request.POST.get("ratingValue"),
                headline = review_form.cleaned_data.get('headline'),  
                body = review_form.cleaned_data.get('body'),
                ticket = linked_ticket
            )
            new_review.save()
            messages.success(request, f"Critique validée pour l'oeuvre suivante: {new_ticket.title}")
            return redirect('../')
    context = {
        'ticket_form': ticket_form,
        'review_form': review_form
    }
    return render(request, 'flux/create_review.html', context)

@login_required
def create_ticket(request):
    form = TicketForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            new_ticket = Ticket.objects.create(
                user = User.objects.get(pk=request.user.id),
                title = form.cleaned_data.get('title'),
                description = form.cleaned_data.get('description'),
                picture = form.cleaned_data.get('picture'),
            )
            new_ticket.save()
            messages.success(request, f"Critique demandée pour l'oeuvre suivante: {new_ticket.title}") #pourquoi sur homepage? Oo
            time.sleep(2)
            return redirect('../')
    context = {'form': form}
    return render(request, 'flux/create_ticket.html', context)

@login_required
def answer_ticket(request, ticket_number):
    ticket = Ticket.objects.get(id=ticket_number)
    form = ReviewForm(request.POST)
    if request.method =='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = Review.objects.create(
                user = User.objects.get(pk=request.user.id),
                rating = request.POST.get("ratingValue"),
                headline = form.cleaned_data.get('headline'),  
                body = form.cleaned_data.get('body'),
                ticket = ticket
            )
            new_review.save()
            return redirect('../')
    context = {
        'ticket': ticket,
        'form': form,
        'reviewuser': request.user,
    }
    return render(request, 'flux/answer_ticket.html', context)


