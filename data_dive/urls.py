from django.urls import path
from data_dive.views import (
    index,
    show_category,
    add_category,
    add_page,
    goto_url,
    like_category_view,
    search_category_view,
)

app_name = 'data_dive'

urlpatterns = [
    path('', index, name='index'),
    path('category/<slug:category_name_slug>/',
         show_category, name='show_category'),
    path('add_category/', add_category, name='add_category'),
    path('add_page/', add_page, name='add_page'),
    path('goto/', goto_url, name='goto_url'),
    path('like_category/', like_category_view, name='like_category'),
    path('search_category/', search_category_view, name='search_category')
]
