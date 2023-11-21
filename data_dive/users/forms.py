from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import UserProfile



class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length=128, required=True)

    class Meta:
        model = get_user_model()
        fields = ['name', 'email', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile

        fields = ['website_url', 'picture']

    def save(self,user=None,files=None, commit=True):
        profile : UserProfile = super(UserProfileForm, self).save(commit=False)

        # Adding user one to one relationship with userProfile if user arent already
        if user:
            profile.user = user

        # Adding picture
        if files and 'picture' in files:
            profile.picture = files['picture']
            profile.picture.name = profile.get_profile_filename(str(files['picture']))

        if commit:
            profile.save()
        return profile

class LoginUserForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text="Email")
    password = forms.CharField(max_length=2048, widget=forms.PasswordInput(), help_text="Password")



class UserAdminChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = get_user_model()
        field_classes = {"email": forms.EmailField}


class UserAdminCreationForm(admin_forms.UserCreationForm):
    """
    Form for User Creation in the Admin Area.
    To change user signup, see UserSignupForm and UserSocialSignupForm.
    """

    class Meta(admin_forms.UserCreationForm.Meta):
        model = get_user_model()
        fields = ("email",)
        field_classes = {"email": forms.EmailField}
        error_messages = {
            "email": {"unique": _("This email has already been taken.")},
        }
