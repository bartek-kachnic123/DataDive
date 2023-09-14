from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from users.models import UserProfile

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=128, required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile

        fields = ['website_url', 'picture']