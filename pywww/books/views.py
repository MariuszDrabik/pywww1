from django.http import request
# from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Book, Author


def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books_list': books})


def book_detail(request, year, book):
    book = get_object_or_404(Book, slug=book, created__year=year)
    book_tags = book.tags.all()
    
    return render(request, "books/book_detail.html", {"book": book, "tags": book_tags})

