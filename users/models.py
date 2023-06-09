from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.db.models.signals import post_save
from django.dispatch import receiver


def profile_image_upload_path(instance, filename):
    """ defining the profile image upload path """
    return f"profiles/{instance.user.username}/{filename}"


class Profile(models.Model):
    """ Profile form """
    user = models.OneToOneField(
        User, related_name="profile",
        on_delete=models.CASCADE
    )
    image = ResizedImageField(
        size=[90, 90],
        quality=100,
        upload_to="profiles/",
        force_format="WEBP",
        blank=True,
        null=True,
    )
    keyboards = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        """ Define the self string """
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """ Creates a profile for user when they register on the website
    Got help from CI tutors implementing this """

    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
