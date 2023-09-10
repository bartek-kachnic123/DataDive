from django.urls import path
from data_dive import views

app_name = 'data_dive'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('add_page/', views.add_page, name='add_page')
]