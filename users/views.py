from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from users.forms import (
    RegisterUserForm,
    UserProfileForm,
    LoginUserForm
)
from users.utils import user_authenticate
# Create your views here.


def register(request):
    is_registered = False

    if request.method == 'POST':
        register_user_form = RegisterUserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if register_user_form.is_valid() and profile_form.is_valid():
            user = register_user_form.save() 

            profile_form.save(user, request.FILES)
            is_registered = True
        else:
            print(register_user_form.errors, profile_form.errors)
    else:

        register_user_form = RegisterUserForm()
        profile_form = UserProfileForm()
    
    context_dict = {
        'title' : 'Register',
        'register_user_form' : register_user_form,
        'profile_form' : profile_form,
        'is_registered': is_registered
    }

    return render(request, 'users/register.html', context=context_dict)

def user_login(request):
    login_user_form = LoginUserForm()
    if request.method == 'POST':
        login_user_form = LoginUserForm(request.POST)

        if login_user_form.is_valid():
            user = user_authenticate(login_form=login_user_form)
            
            if user and user.is_active:
                login(request, user)
                return redirect(reverse('data_dive:index'))
            elif user:
                login_user_form.add_error('password', 'Account is disabled!')
            else:
                login_user_form.add_error('password', 'Invalid username, email or password')

    context_dict = {
        'title' : 'Login',
        'login_user_form' : login_user_form
    }
    return render(request, 'users/login.html', context=context_dict)