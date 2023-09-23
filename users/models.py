from django.db import models
from django.contrib.auth.models import User
from users.storage import ProfileImageStorage
# Create your models here.


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
            self.picture = files['picture']
            self.picture.name = self.get_profile_filename(str(files['picture']))

        self.save()

    def get_profile_filename(self, filename: str) -> str:
        img_type = filename[filename.rfind('.'):]

        return f'profile__{self.user.username}{img_type}'
