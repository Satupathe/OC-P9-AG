from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Follow
from .forms import FollowForm


@login_required
def follow(request):
    user_obj = User.objects.get(username=request.user)
    followed_users = Follow.objects.filter(user__exact=request.user)
    check_followers = Follow.objects.filter(followed_user__exact=request.user)

    # Partie pour ajouter un utilisateur à suivre
    form = FollowForm(request.POST)
    if request.method == "POST":
        if "follow" in request.POST:
            form = FollowForm(request.POST)
            if form.is_valid():
                result = form.cleaned_data.get("name")
                try:
                    followed_user = User.objects.get(username=result)
                    if followed_user == user_obj:
                        messages.error(
                            request,
                            "Erreur: vous ne pouvez pas vous suivre vous-même, merci d'essayer à nouveau!",
                        )
                        return redirect("follow")
                    else:
                        new_follow = Follow.objects.create(
                            user=request.user, followed_user=followed_user
                        )
                        new_follow.save()
                        messages.success(
                            request,
                            f"Vous suivez maintenant l'utilisateur {new_follow.followed_user}.",
                        )
                        return redirect("follow")
                except ObjectDoesNotExist:
                    messages.error(request, f"L'utlisateur {result} est introuvable!")
                    return redirect("follow")

        elif "unfollow" in request.POST:
            unfollow_name = request.POST.get("unfollow")
            followed_user = User.objects.get(username=unfollow_name)
            followed_users.get(followed_user__exact=followed_user).delete()
            return redirect("follow")

    context = {
        "form": FollowForm,
        "user_obj": user_obj,
        "followed_users": followed_users,
        "check_followers": check_followers,
    }
    return render(request, "follow/follow.html", context)
