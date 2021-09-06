from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Review, Ticket
from django_starfield import Stars


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']
        rating = forms.IntegerField(widget=Stars)

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'picture']