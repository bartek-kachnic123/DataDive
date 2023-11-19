from django.contrib import admin
from .models import UserProfile
from .admin_models import UserProfileAdmin
# Register your models here.


admin.site.register(UserProfile, UserProfileAdmin)