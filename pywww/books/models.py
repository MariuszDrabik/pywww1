from django.db import models
from django.urls import reverse
from datetime import datetime


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.pk} {self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=550)
    slug = models.SlugField(max_length=255, unique_for_date='created')
    description = models.TextField()
    available = models.BooleanField(default=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return f'{self.pk} Tytuł: {self.title} {self.author}'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:book_detail", args=[self.created.year, self.slug])
