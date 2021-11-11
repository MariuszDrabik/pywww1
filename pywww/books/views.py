from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Book, Author


def books_index(request):
    books = Book.objects.all()
    return HttpResponse("Tu bedom ksiązki")
