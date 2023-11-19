from django.core import serializers
from .models import Category


class CategorySerializer:
    model = Category

    def serialize(query_set):    # noqa
        data = serializers.serialize("json", query_set, fields=["name", "slug"])
        return data
