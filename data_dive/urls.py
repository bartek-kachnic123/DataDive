from django.urls import path
from data_dive.views import (
    index,
    show_category,
    add_category,
    add_page,
    goto_url
)

app_name = 'data_dive'

urlpatterns = [
    path('', index, name='index'),
    path('category/<slug:category_name_slug>/', show_category, name='show_category'),
    path('add_category/', add_category, name='add_category'),
    path('add_page/', add_page, name='add_page'),
    path('goto/', goto_url, name='goto_url')
]
