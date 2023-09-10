import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'data_dive_django_project.settings')
import django
django.setup()

from data_dive import models


def add_Page(category, title, url, views=0) -> models.Page:
    page, is_created = models.Page.objects.get_or_create(
        category=category, title=title)

    if is_created:
        page.url = url
        page.views = views
        page.save()
    return page


def add_Category(name) -> models.Category:
    category, is_created = models.Category.objects.get_or_create(name=name)

    if is_created:
        category.save()
    return category


def populate():
    print("Starting script...")
    django_pages = [
        {'title': 'Tango with Django', 'url': 'https://www.tangowithdjango.com/'}
    ]
    flask_pages = [
        {'title': 'Mega-Tutorial',
            'url': 'https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world'}
    ]
    python_pages = [
        {'title': 'Python Module of the week',
            'url': 'http://pymotw.com/2/index.html'}
    ]
    categories_data = {
        'Django': {'pages': django_pages},
        'Flask': {'pages': flask_pages},
        'Python': {'pages': python_pages}
    }

    for category_name, category_pages in categories_data.items():
        category = add_Category(category_name)
        for page in category_pages['pages']:
            add_Page(category, page['title'], page['url'])

    for category in models.Category.objects.all():
        for page in models.Page.objects.filter(category=category):
            print(f'Category: {category} : {page}')

    print("End")

if __name__ == "__main__":
    populate()