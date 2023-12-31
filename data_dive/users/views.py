from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import (
    login,
    logout,
    authenticate,
)

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpRequest
from .forms import (
    RegisterUserForm,
    UserProfileForm,
    LoginUserForm
)
from .models import UserProfile
# Create your views here.


def register(request):
    is_registered = False

    if request.method == 'POST':
        register_user_form = RegisterUserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if register_user_form.is_valid() and profile_form.is_valid():
            user: User = register_user_form.save()

            profile_form.save(user, request.FILES)
            is_registered = True
            if user:
                login(request, user)
            return redirect(reverse('page_categorizer:index'))
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
            email = login_user_form.cleaned_data.get('email')
            password = login_user_form.cleaned_data.get('password')

            user = authenticate(email=email, password=password)

            if user and user.is_active:
                login(request, user)
                return redirect(reverse('page_categorizer:index'))
            elif user:
                login_user_form.add_error('password', 'Account is disabled!')
            else:
                login_user_form.add_error(
                    'password', 'Invalid name, email or password')

    context_dict = {
        'title': 'Login',
        'login_user_form': login_user_form
    }
    return render(request, 'users/login.html', context=context_dict)


@login_required
def user_logout(request):
    logout(request)

    return redirect(reverse('page_categorizer:index'))


class UpdateProfileView(View):
    @method_decorator(login_required)
    def get(self, request: HttpRequest):
        profile_form = UserProfileForm()
        user_profile, context_dict = self.get_userprofile_and_context(
            request.user, profile_form)
        profile_form.initial = {'website_url': user_profile.website_url, 'picture': user_profile.picture,
                                }
        return render(request, 'users/profile.html', context=context_dict)

    @method_decorator(login_required)
    def post(self, request: HttpRequest):
        profile_form = UserProfileForm(request.POST, request.FILES)
        user_profile, context_dict = self.get_userprofile_and_context(
            request.user, profile_form)
        if profile_form.is_valid():
            user_profile.update(cleaned_data=profile_form.cleaned_data,
                                files=request.FILES)

            return redirect(reverse('users:profile'))
        else:
            return render(request, 'users/profile.html', context=context_dict)

    def get_userprofile_and_context(self, _user: User, profile_form: UserProfileForm):
        user_profile = UserProfile.objects.get(user=_user)

        profile_url = None
        if user_profile.picture:
            profile_url = user_profile.picture.url

        context_dict = {'profile_form': profile_form,
                        'profile_url': profile_url}
        return (user_profile, context_dict)


update_profile_view = UpdateProfileView.as_view()
