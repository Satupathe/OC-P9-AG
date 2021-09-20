from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.flux, name='flux'),
    path('quitter/', views.logout_user, name='logout_user'),
    path('create_review/', views.create_review, name='create_review'),
    path('ticket/', views.create_ticket, name='ticket'),
    path('answer_ticket/<str:ticket_number>', views.answer_ticket, name='answer_ticket'),
    path('follow/', include('follow.urls')),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)