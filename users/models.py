from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField


class Profile(models.Model):

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    image = ResizedImageField(
        size=[100, 100],
        quality=75,
        upload_to="profiles/",
        force_format="WEBP",
        blank=False,
    )
    keyboards = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)