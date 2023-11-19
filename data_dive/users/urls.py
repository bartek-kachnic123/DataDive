from django.urls import path
from .views import (
    register,
    user_login,
    user_logout,
    update_profile_view,
)

app_name = 'users'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('profile/', update_profile_view, name='profile')
]