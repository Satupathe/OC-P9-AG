from django.db import models
from django.contrib.auth.models import User

class Follow(models.Model):
    following = models.ManyToManyField(User)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner', null=True)
    
    @classmethod
    def add_follow(cls, user, new_follow):
        follow, created = cls.objects.get_or_create(
            user=user
        )
        follow.following.add(new_follow)

    @classmethod
    def loose_follow(cls, user, new_follow):
        follow, created = cls.objects.get_or_create(
            user=user
        )
        follow.following.remove(new_follow)

