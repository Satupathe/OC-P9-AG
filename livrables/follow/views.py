from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Follow
from .forms import FollowForm


"""def follow(request, operation, pk):
    follow = Follow.objects.get(user=request.user)
    follows = follow.following.all()
    following = Follow.objects.get(pk=pk)
    #follower = Users.objects.filter() trouver dans le lien user --> follow ou dans l'ensemble des follow? si dans following il y a user
    if operation == 'add':
        Follow.add_follow(request.user, following)
    elif operation == 'remove':
        Follow.loose_follow(request.user, following)

    
    context = {
        'following':following,
        'follows':follows,
    }
    return render(request, 'follow.html', context)"""

@login_required
def profile(request):
    user_obj = User.objects.get(username=request.user)
    session_following, create = Follow.objects.get_or_create(user=user_obj)
    following_field, create = Follow.objects.get_or_create(user=user_obj.id)
    check_user_followed = Follow.objects.filter(user=user_obj)
    

    #Partie pour ajouter un utilisateur à suivre
    check_follower = Follow.objects.get(user=request.user) #username?
    form = FollowForm(request.POST)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = FollowForm(request.POST)
            if form.is_valid():
                result = form.cleaned_data.get('name')
                followed_user = User.objects.get(username=result)
                if check_follower.following.filter(username=result).exists():
                    pass
                else:
                    add_usr = Follow.objects.get(user=user_obj)
                    add_usr.following.add(followed_user)
    context = {
        'form': FollowForm,
        'user_obj': user_obj,
        'session_following': session_following,
        'following_field': following_field,
        'check_user_followed': check_user_followed,
        'check_follower': check_follower,
    }
    return render(request, 'follow/follow.html', context)
                



    """new_followed_user = User.objects.get(username=followed_user_name)
    form = FollowForm
    
    if new_followed_user != user_obj:
        if check_follower.owner.filter(username=new_followed_user).exist():
            pass
        elif check_follower.owner.filter(username=new_followed_user).exist() is False:
            add_usr = Follow.objects.get(user=user_obj)
            add_usr.following.add(new_followed_user)"""
    context = {'user_obj': user_obj,'followers':check_user_followers, 'following_field': following_field,'is_followed':is_followed, 'followed_user_name': followed_user_name}
    return render(request, 'follow/follow.html', context)
    
"""@login_required
def follow(request):
    user_obj = User.objects.get(username=request.user)
    check_follower = Follow.objects.get(user=user_obj.id)
    is_followed = False
    if other_user.name != session_user:
        if check_follower.another_user.filter(name=other_user).exists():
            add_usr = Follow.objects.get(user=get_user)
            add_usr.another_user.remove(other_user)
            is_followed = False
            return redirect(f'/profile/{session_user}')
        else:
            add_usr = Follow.objects.get(user=get_user)
            add_usr.another_user.add(other_user)
            is_followed = True
            return redirect(f'/profile/{session_user}')

        return redirect(f'/profile/{session_user}')
    else:
        return redirect(f'/profile/{session_user}')"""

"""@login_required
def follow(request):
    user_obj = User.objects.get(username=request.user)
    check_follower = Follow.objects.get(user=user_obj.id) #username?
    followed_user_name = request.POST.get('followed_user_name')
    new_followed_user = User.objects.get(username=followed_user_name)
    form = FollowForm
    
    if new_followed_user != user_obj:
        if check_follower.owner.filter(username=new_followed_user).exist():
            pass
        elif check_follower.owner.filter(username=new_followed_user).exist() is False:
            add_usr = Follow.objects.get(user=user_obj)
            add_usr.following.add(new_followed_user)
    context = {
        'form': FollowForm,
    }
    return render(request, )"""
    



"""users = User.objects.all()
users = User.objects.exclude(id=request.user.id)#permet d'exclure l'utilisateur connecté de la liste des utilisateurs disponibles.
#add users to context and send it to the page

template --> permet juste de mettre l'ensemble des utilisateur sur la page d'accueil
{% url 'account: view_profile' %}

#dans le modèle créer un modèle friend ou following
class Friend(models.Model):
    users = models.ManyToManyField(User)
#possibilité de l'ajouter à admin

#Penser à utiliser create aussi pour l'ajout d'amis dans le modèle
friend = Friend()
friend.save()
friend.users.add(User.objects.first(), User.objects.last()
--> car il faut enregister un champs friend avant de sauvegarder un friend)"""
