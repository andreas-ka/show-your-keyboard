from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


def profile_image_upload_path(instance, filename):
    return f"profiles/{instance.user.username}/{filename}"


class Profile(models.Model):
    # Profile form #
    user = models.OneToOneField(
        User, related_name="profile", 
        on_delete=models.CASCADE
    )
    image = ResizedImageField(
        size=[100, None],
        quality=100,
        upload_to="profiles/",
        force_format="WEBP",
        blank=True,
        null=True,
    )
    keyboards = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

# Creates a profile for user when they register on the website #
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()