from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey, OneToOneField



class Ticket(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    picture = models.ImageField(null=True, upload_to='images/')
    time_created = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rating = models.IntegerField()
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    time_created = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='User', default=1)
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following', default=1)