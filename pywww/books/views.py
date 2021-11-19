from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Book, Author


def books_index(request):
    books = Book.objects.all()
    return HttpResponse("Tu bedom ksiązki")


def book_detail(book):
    # unique_slug = get_object_or_404(Book)
    # print(unique_slug)
    # return render(request, "books/books_detail.html", {"book": unique_slug})
    book1 = Book.objects.all()[1]
    print(book1)
    return HttpResponse(book1)
