from django.core import serializers
from data_dive.models import Category


class CategorySerializer:
    def serialize(query_set):    # noqa
        data = serializers.serialize("json", query_set, fields=["name", "slug"])
        return data
