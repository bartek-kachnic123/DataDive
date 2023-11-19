from django.contrib import admin

from .models import Category, Page
from .admin_models import CategoryAdmin, PageAdmin


# Register your models here.
admin.site.register(Category, CategoryAdmin)

admin.site.register(Page, PageAdmin)