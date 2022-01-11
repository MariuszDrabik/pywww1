from django.contrib import admin
from .models import Author, Book


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'published', 'available')
    list_filter = ('published', 'available')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Author)
admin.site.register(Book, BooksAdmin)
