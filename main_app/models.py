from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

# class MainUser(models.Model):
#     username= models.CharField(max_length=150)
    
class Account(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Movie(models.Model):
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    description = models.TextField()
    poster = models.ImageField(upload_to='poster')


class TV(models.Model):
    title = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    description = models.TextField()
    poster = models.ImageField(upload_to='poster')

# class Views(models.Model):
#     date = models.DateTimeField('view date and time')
