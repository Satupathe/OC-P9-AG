from django.db import models

class User(models.Model):
    nom = models.CharField(max_length=200,null=True)
    telephone = models.CharField(max_length=200,null=True)
    date_creation = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.nom
        
