from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveBigIntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField(max_length=1024)
    views = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title
