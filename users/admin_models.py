from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__','get_user_email', 'website_url')
    list_select_related = True

    def get_queryset(self, request):
        return super(UserProfileAdmin,self).get_queryset(request).select_related('user')
    
    @admin.display(description='Email', ordering='user__email')
    def get_user_email(self, obj):
        return obj.user.email
    
   