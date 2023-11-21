from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .storage import ProfileImageStorage
from .managers import UserManager
# Create your models here.

class User(AbstractUser):
    """
    Default custom user model for DataDive Project.
    """

    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=254)
    first_name = None
    last_name = None
    email = models.EmailField(_("email address"), unique=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website_url = models.URLField(blank=True)
    picture = models.ImageField(
        upload_to='profile_images/', storage=ProfileImageStorage(), blank=True)

    def __str__(self):
        return self.user.username

    def update(self, cleaned_data: dict | None = None, files: dict | None = None):
        if cleaned_data and 'website_url' in cleaned_data:
            self.website_url = cleaned_data['website_url']

        if files and 'picture' in files:
            self.picture.delete(save=False) # Delete previous profile
            self.picture = files['picture']
            self.picture.name = self.get_profile_filename(str(files['picture']))

        self.save()

    def get_profile_filename(self, filename: str) -> str:
        img_type = filename[filename.rfind('.'):]

        return f'profile__{self.user.username}{img_type}'
