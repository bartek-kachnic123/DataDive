from django.contrib import admin

from data_dive.models import ( 
    Category, Page
)
from data_dive.admin_models import (
    CategoryAdmin, PageAdmin
)



# Register your models here.
admin.site.register(Category, CategoryAdmin)

admin.site.register(Page, PageAdmin)