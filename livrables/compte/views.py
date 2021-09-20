from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def home_page(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        nxt = request.GET.get("next", None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if nxt is not None:
                return redirect(nxt)
            return redirect('flux')   
        else: messages.info(request, "Utilisateur et/ou mot de passe incorrect")
    context = {}
    return render(request, 'compte/home_page.html', context)

def sign_in(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'compte/sign_up.html', {'form': form})

def redirect_home(request):
  return HttpResponseRedirect('/compte/')


def logout_user(request):
    logout(request)
    return redirect('home')