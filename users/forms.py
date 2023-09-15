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

    def save(self,user=None,files=None, commit=True):
        profile = super(UserProfileForm, self).save(commit=False)

        # Adding user one to one relationship with userProfile
        if user:
            profile.user = user

        # Adding picture
        if files and 'picture' in files:
            profile.picture = files['picture']

        if commit:
            profile.save()
        return profile

class LoginUserForm(forms.Form):
    username_or_email = forms.CharField(max_length=150, help_text="Username or Email")
    password = forms.CharField(max_length=2048, widget=forms.PasswordInput())
    