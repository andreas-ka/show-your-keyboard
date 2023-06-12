from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from cloudinary_storage.storage import RawMediaCloudinaryStorage
from cloudinary.models import CloudinaryField



def profile_image_upload_path(instance, filename):
    return f"profiles/{instance.user.username}/{filename}"


class Profile(models.Model):

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    image = CloudinaryField('image', blank=True, null=True)
    keyboards = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)