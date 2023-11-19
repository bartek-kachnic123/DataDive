from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

from .forms import CategoryForm, PageForm
from .models import Category, Page
from .utils import get_category_list
from .serializers import CategorySerializer

# Create your views here.


def index(request):
    context_dict = {
        'title': 'Main page context'
    }
    # Get top 5 categories by number of likes"
    categories_list = Category.objects.order_by('-likes')[:5]
    context_dict['categories_list'] = categories_list

    return render(request, 'page_categorizer/index.html', context=context_dict)


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

    return render(request, 'page_categorizer/category.html', context=context_dict)


@login_required
def add_category(request):
    context_dict = {'title': 'Add a Category'}
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/dive/')
        else:
            print(form.errors)

    context_dict['form'] = form

    return render(request, 'page_categorizer/add_category.html', context=context_dict)


@login_required
def add_page(request):
    context_dict = {'title': 'Add a Page'}
    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            category_slug = form.cleaned_data['category'].slug
            return redirect(reverse('page_categorizer:show_category',
                                    kwargs={'category_name_slug': category_slug
                                            }))

        else:
            print(form.errors)
    context_dict['form'] = form

    return render(request, 'page_categorizer/add_page.html', context=context_dict)


def goto_url(request: HttpRequest):
    if request.method == 'GET':
        page_id = request.GET.get('page_id')

        try:
            selected_page = Page.objects.get(id=page_id)
        except Page.DoesNotExist:
            # add message here
            return redirect(reverse('page_categorizer:index'))

        selected_page.views = F('views') + 1
        selected_page.save()

        return redirect(selected_page.url)


class LikeCategoryView(View):

    @method_decorator(login_required)
    def get(self, request: HttpRequest):
        category_id = request.GET.get('category_id')

        try:
            category = Category.objects.get(id=int(category_id))
        except Category.DoesNotExist or ValueError:
            return HttpResponse(-1)
        user = get_user(request)
        is_liked = None
        if category.is_liked_by(user):
            category.likes = F('likes') - 1
            category.unlike_category(user)
            is_liked = True
        else:
            category.likes = F('likes') + 1
            category.like_category(user)
            is_liked = False

        category.save()

        category.refresh_from_db()
        data_dict = {
            'likes': category.likes,
            'is_liked': is_liked
        }
        return JsonResponse(data=data_dict)


like_category_view = LikeCategoryView.as_view()


class SearchCategoryView(View):
    def get(self, request: HttpRequest, *args, **kwargs): # noqa
        query = request.GET.get('query', '') # noqa
        result_list = get_category_list(max_results=5, contains=query)

        data_dict = {
            'result_list': CategorySerializer.serialize(query_set=result_list),
        }
        return JsonResponse(data=data_dict)


search_category_view = SearchCategoryView.as_view()
