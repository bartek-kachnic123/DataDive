from django.contrib import admin

from data_dive import models
from data_dive import admin_models



# Register your models here.
admin.site.register(models.Category, admin_models.CategoryAdmin)

admin.site.register(models.Page, admin_models.PageAdmin)