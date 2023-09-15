from django.contrib import admin
from users.models import UserProfile
from users.admin_models import UserProfileAdmin
# Register your models here.


admin.site.register(UserProfile, UserProfileAdmin)