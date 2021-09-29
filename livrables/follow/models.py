from django.db import models
from django.contrib.auth.models import User


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
