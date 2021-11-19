from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=550)
    description = models.TextField()
    available = models.BooleanField(default=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.pk} Tytuł: {self.title} {self.author}'
