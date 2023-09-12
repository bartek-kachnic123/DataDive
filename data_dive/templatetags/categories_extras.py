from django import template
from data_dive import models


register = template.Library()

@register.simple_tag
def get_category_list(current_category = None):
    return {'all_categories_list' : models.Category.objects.all(),
            'current_category' : current_category}