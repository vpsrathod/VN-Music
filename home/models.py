from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    
    # this is for profile 
    # models.py

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    name = models.CharField(max_length=221,blank =True)
    email =models.EmailField(max_length=254,blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

    