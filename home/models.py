from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from PIL import Image
from django.urls import reverse
from datetime import datetime, date



class Post(models.Model):
    user = models.ForeignKey(User, related_name="post_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=1000, null=False, blank=False)
    case = models.CharField(max_length=100)
    switches = models.CharField(max_length=200)
    keycaps = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=200)
    image = ResizedImageField(
        size=[300, None],
        quality=100,
        upload_to="home/",
        force_format="WEBP",
        blank=True,
        null=True,
    )
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.user)

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    user_profile = models.ForeignKey(User, related_name="user_profile", on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body}"