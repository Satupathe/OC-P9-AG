from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name= 'home'),
    path('inscription/', views.sign_in, name= 'sign_up'),
    path('quitter/', views.logout_user, name= 'logout_user'),
    path('redirect/', views.redirect_home, name='returner'),
    path('flux/', include('flux.urls')),
]

