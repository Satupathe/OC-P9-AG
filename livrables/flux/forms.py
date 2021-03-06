from django.forms import ModelForm
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
