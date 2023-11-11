from data_dive.models import Category


def get_category_list(max_results=0, contains=''):
    """
    This function queries the database for categories
    that contain a specified substring within their names.
    The search is case-insensitive, allowing for more flexible matching.
    """
    category_list = []

    if contains:
        category_list = Category.objects.filter(name__icontains=contains)

    if 0 < max_results < len(category_list):
        category_list = category_list[:max_results]

    return category_list
