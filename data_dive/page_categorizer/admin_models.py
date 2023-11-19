from django.contrib import admin


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'likes', 'views')

    prepopulated_fields={'slug' : ('name',)}