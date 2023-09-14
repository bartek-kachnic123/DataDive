from django.shortcuts import render

from users.forms import (
    RegisterUserForm,
    UserProfileForm
)
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

    return render(request, 'users/templates/register.html', context=context_dict)