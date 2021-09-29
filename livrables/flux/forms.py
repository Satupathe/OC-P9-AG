from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Review, Ticket


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'body']
        labels = {
            'headline': 'Titre de la critique',
            'body': "Critique"
        }

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'picture']
        labels = {
            'title': 'Titre',
            'picture': 'Image'
        }