from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from PIL import Image


class Post(models.Model):
    user = models.ForeignKey(User, related_name="post_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    case = models.CharField(max_length=100)
    switches = models.CharField(max_length=200)
    keycaps = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=200)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.user)
