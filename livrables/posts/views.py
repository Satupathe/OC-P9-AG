from itertools import chain
from operator import attrgetter
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib import messages
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
    #user_reviews = Review.objects.filter(user__exact=user_obj).exclude(ticket__user=user_obj)
    user_reviews = Ticket.objects.exclude(user__exact=user_obj).filter(review__user__exact=user_obj).annotate(review_user=F('review__user__username'),
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

    if request.method =='POST':
        if 'suppress' in request.POST:
            supress_id = request.POST.get("suppress")
            ticket_to_supress = Ticket.objects.get(id=supress_id)
            if ticket_to_supress.user == request.user:
                ticket_to_supress.delete()
            else:
                review_to_suppress = Review.objects.get(ticket__id=supress_id) #get ou filter à tester
                review_to_suppress.delete()

    
    # récupérer l'utilisateur connecté ok
    # trouver les tickets postés par l'utilisateur ok
    # regarder s'il existe des reviews associées ok 
    # si oui regarder si la review est faite par l'utilisateur ok
        # si oui l'ajouter à la récupération du ticket ok
        # si non ne pas montrer la montrer mais dire qu'il y en a une ok
    # si non récupérer simplement le ticket et cacher les champs ok
    # récupérer dans les tickets qui ne sont pas de l'utilisateur, les reviews de l'utilisateur ok
    # combiner le tout avec chain ok
    # récupérer les dates de création ok
    # afficher par ordre chronologique décroissant ok --> vérifier l'affichage des étoiles
    # mettre une pagination ok

    # Créer un bouton supprimer le post récupérant un formulaire et un input de nom "delete" ok
    # récupérer l'id du post via le bouton de suppression ok
    # supprimer l'élément dans le modèle correspondant ok
    # si ticket.user = request.user --> supprimer le ticket ok
    # si ticket.user != request.user --> supprimer la review ok
    # prévoir un message de validation de la suppression
    # actualiser l'affichage de la page pour voir les modifications. --> voir ce qui cloche actuellement
    

    # créer un bouton pour modifier le post en récupérant un formulaire et un input de nom "modify"
    # récupérer la pk du post via le bouton de modification 
    # l'envoyer via l'url sur la page de modification

    context = {
        'user_tickets': user_tickets,
        'tickets_and_review': tickets_and_reviews,
        'user_reviews': user_reviews,
        'total_posts': total_posts,
        'ordered_total_posts': ordered_total_posts,
        'tickets':tickets,
        'paginate':True,
        'user': request.user,
    }
    return render(request, 'posts/posts.html', context)

@login_required
def modify(request, ticket_number):
    user_obj = User.objects.get(username=request.user)
    ticket = Ticket.objects.get(id=ticket_number)
    ticket_form = TicketForm(instance=ticket)
    review_form = ReviewForm(instance=ticket)
    result = []
    actual_form = []
    associated_review = None

    try:
        associated_review = Review.objects.get(ticket__id=ticket_number)
        if ticket.user == user_obj and associated_review.user == user_obj:
            if request.method =='POST':
                if ticket_form.is_valid():
                    ticket.update(title=ticket_form.cleaned_data.get('title'),
                                  description=ticket_form.cleaned_data.get('description'),
                                  picture=ticket_form.cleaned_data.get('picture')
                                  )
                if review_form.is_valid():
                    associated_review.update(headline=ticket_form.cleaned_data.get('headline'),
                                             body=ticket_form.cleaned_data.get('body'),
                                             rating=ticket_form.cleaned_data.get('rating')
                                             )
                return redirect("posts")


        elif ticket.user == user_obj and associated_review.user != user_obj:
            if request.method =='POST':
                ticket_form = TicketForm(request.POST, instance=ticket)
                if ticket_form.is_valid():
                    ticket = ticket_form.save(commit=False)
                    ticket.title = ticket_form.cleaned_data.get('title')
                    ticket.description = ticket_form.cleaned_data.get('description')
                    ticket.picture = ticket_form.cleaned_data.get('picture')
                    ticket_form.save()
                return redirect("posts")

        elif ticket.user != user_obj and associated_review.user == user_obj:
            if request.method =='POST':
                review_form = ReviewForm(request.POST, instance = ticket)
                if review_form.is_valid():
                    review_form.save(commit=False)
                    return redirect("posts")

    except ObjectDoesNotExist:
        if request.method =='POST':
            if ticket_form.is_valid():
                ticket = ticket_form.save(commit=False)
                ticket.title = ticket_form.cleaned_data.get('title')
                ticket.description = ticket_form.cleaned_data.get('description')
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
    # prévoir un autre vue pour la modification du post ok
    # récupérer les informations de l'utilisateur connecté ok
    # récupérer les informations du post à modifier grâce à la pk envoyée par le template
    # les afficher dans un formulaire (remettre les infos dans chaque lien et field)
    # créer un bouton envoyer dans le formulaire
    # sauvegarder les changements en faisant un update des infos de la db (CRUD)
    # prévoir un message de validation de la modification
    # retourner sur la page des posts