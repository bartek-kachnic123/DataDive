from typing import Any, Dict
from django import forms

from data_dive.models import ( 
    Category, Page
)

import re


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Enter a category name")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.SlugField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=None, initial=Category.objects.first())
    title = forms.CharField(max_length=128, help_text="Enter a title for page", required=True)
    url = forms.URLField(
        max_length=1024, help_text="Enter a url field to page", required=True)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page

        fields = ('category', 'title', 'url')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].queryset = Category.objects.all()

    def clean(self) -> Dict[str, Any]:
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # if url doesnt start with https:// and url is not empty
        url = re.sub(r'http[s]:[\/]+', '', url)

        if url:
            url = f'https://{url}'
            cleaned_data['url'] = url

        return cleaned_data
