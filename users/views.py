from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import (
    login,
    logout
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpRequest
from users.forms import (
    RegisterUserForm,
    UserProfileForm,
    LoginUserForm
)
from users.models import UserProfile
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
        'title': 'Register',
        'register_user_form': register_user_form,
        'profile_form': profile_form,
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
                login_user_form.add_error(
                    'password', 'Invalid username, email or password')

    context_dict = {
        'title': 'Login',
        'login_user_form': login_user_form
    }
    return render(request, 'users/login.html', context=context_dict)


@login_required
def user_logout(request):
    logout(request)

    return redirect(reverse('data_dive:index'))


class UpdateProfileView(View):
    @method_decorator(login_required)
    def get(self, request: HttpRequest):
        user_profile = UserProfile.objects.get(user=request.user)
        profile_form = UserProfileForm(
            initial={'website_url': user_profile.website_url, 'picture': user_profile.picture,
                     })
        context_dict = {'profile_form': profile_form,
                        'profile_url': user_profile.picture.url}
        return render(request, 'users/profile.html', context=context_dict)

    @method_decorator(login_required)
    def post(self, request: HttpRequest):
        profile_form = UserProfileForm(request.POST, request.FILES)
        user_profile = UserProfile.objects.get(user=request.user)

        context_dict = {'profile_form': profile_form,
                        'profile_url': user_profile.picture.url}
        if profile_form.is_valid():
            user_profile.update(cleaned_data=profile_form.cleaned_data,
                                files=request.FILES)

            return redirect(reverse('users:profile'))
        else:
            return render(request, 'users/profile.html', context=context_dict)


update_profile_view = UpdateProfileView.as_view()
