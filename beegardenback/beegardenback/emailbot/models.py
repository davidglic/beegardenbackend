from django.db import models
from django.apps import apps
# Create your models here.


from beegardenbackapp.models import User

class VerToken(models.Model):
    email = models.CharField(max_length=100)
    vertoken = models.IntegerField()

    def __str__(self):
        return self.email
    

