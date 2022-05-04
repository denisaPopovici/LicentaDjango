from django.db import models
import datetime
# Create your models here.
from django.contrib.auth.models import User


class Location(models.Model):
    name = models.CharField(blank=False, null=False, max_length=100, default='Location')
    latitude = models.CharField(blank=False, null=False, max_length=12, default='')
    longitude = models.CharField(blank=False, null=False, max_length=13, default='')
    image = models.ImageField(null=False, blank=False)
    xp = models.IntegerField(null=False, blank=False, default=0)
    description = models.CharField(null=False, blank=False, max_length=400, default='')


class CustomUser(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    about = models.CharField(max_length=150, default="", blank=False)
    image = models.ImageField()
    level = models.IntegerField(default=1, blank=False, null=False)
    xp = models.IntegerField(default=0, blank=False, null=False)


class Level(models.Model):
    objects = models.Manager()
    inferior_limit = models.IntegerField(default=0, blank=False, null=False)
    superior_limit = models.IntegerField(default=0, blank=False, null=False)


class Rating(models.Model):
    objects = models.Manager()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    rating = models.IntegerField(default=0, blank=False, null=False)


class Post(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False, blank=False)
    date = models.DateField(blank=False, null=False, default=datetime.date.today())
    image = models.ImageField(null=False, blank=False)
    description = models.CharField(max_length=400, default="", blank=False, null=False)
    no_likes = models.IntegerField(default=0, blank=False, null=False)
    no_comments = models.IntegerField(default=0, blank=False, null=False)


class VisitedLocations(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False, blank=False)


class UserLikePost(models.Model):
    objects = models.Manager()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False, blank=False)
    text = models.CharField(max_length=150, default="", blank=False, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False)


class Notification(models.Model):
    type = models.CharField(max_length=150, default="", blank=False, null=False)
    notified = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False, related_name="notified")
    notifying = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, blank=False,
                                  related_name="notifying")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    read = models.BooleanField(default=False, blank=False, null=False)


class UserFollow(models.Model):
    objects = models.Manager()
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, default=-1, related_name='follower')
    followed = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False, default=-1, related_name='followed')
