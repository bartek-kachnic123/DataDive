from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.PositiveIntegerField(default=0)
    views = models.PositiveBigIntegerField(default=0)
    slug = models.SlugField(unique=True)

    liked_by_users = models.ManyToManyField(
        User,
        related_name='liked_categories',
        related_query_name='liked_category',
        default=User.objects.none()
        )

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def like_category(self, user: User) -> None:
        self.liked_by_users.add(user)

    def unlike_category(self, user: User) -> None:
        self.liked_by_users.remove(user)

    def is_liked_by(self, user: User) -> bool:
        return self.liked_by_users.contains(user)


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField(max_length=1024)
    views = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return self.title
