from django import template
from ..models import Category


register = template.Library()

@register.simple_tag
def get_category_list(current_category=None):
    return {'all_categories_list': Category.objects.all(),
            'current_category': current_category}
