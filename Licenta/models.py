from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100, default='Location')
    latitude = models.CharField(blank=False, null=False, max_length=12, default='')
    longitude = models.CharField(blank=False, null=False, max_length=13, default='')
    image = models.ImageField(null=False)

class CustomUser(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=150, default="")
    image = models.ImageField()