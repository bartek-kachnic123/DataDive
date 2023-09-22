from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.db.models import F
from data_dive.models import ( 
    Category, Page
)
from data_dive.forms import (
    CategoryForm, PageForm
)
# Create your views here.


def index(request):
    context_dict = {
        'title': 'Main page context'
    }
    # Get top 5 categories by number of likes"
    categories_list = Category.objects.order_by('-likes')[:5]
    context_dict['categories_list'] = categories_list

    return render(request, 'data_dive/index.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category).order_by('-views')

        context_dict['category'] = category
        context_dict['pages'] = pages
        context_dict['title'] = category.name
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'data_dive/category.html', context=context_dict)

@login_required
def add_category(request):
    context_dict = {'title' : 'Add a Category'}
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/dive/')
        else:
            print(form.errors)

    context_dict['form'] = form

    return render(request, 'data_dive/add_category.html', context=context_dict)

@login_required
def add_page(request):
    context_dict = {'title' : 'Add a Page'}
    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            category_slug = form.cleaned_data['category'].slug
            return redirect(reverse('data_dive:show_category', kwargs={'category_name_slug': category_slug}))

        else:
            print(form.errors)
    context_dict['form'] = form

    return render(request, 'data_dive/add_page.html', context=context_dict)


def goto_url(request : HttpRequest):
    if request.method == 'GET':
        page_id = request.GET.get('page_id')

        try:
            selected_page = Page.objects.get(id=page_id)
        except Page.DoesNotExist:
            # add message here
            return redirect(reverse('data_dive:index'))
        
        selected_page.views = F('views') + 1
        selected_page.save()

        return redirect(selected_page.url)