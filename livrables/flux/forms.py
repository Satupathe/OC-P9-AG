from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Review, Ticket


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'body']

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'picture']