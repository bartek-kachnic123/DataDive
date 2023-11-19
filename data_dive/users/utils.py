from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .forms import LoginUserForm


def user_authenticate(login_form : LoginUserForm):
    username_or_email = login_form.cleaned_data.get('username_or_email')
    password = login_form.cleaned_data.get('password')

    # Try if username_or_email is username
    user = authenticate(username=username_or_email, password=password)

    if not user:  # Try if username_or_email is email

        username = User.objects.get(email=username_or_email).username
        user = authenticate(username=username, password=password)
    
    return user



