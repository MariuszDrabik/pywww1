from django.shortcuts import render
from django.http import HttpResponse


def hello_word(request):
    return HttpResponse("Hello Word")


def test(request):
    books = set(['Czysty kod', 'PHP8', 'Dobre praktyki'])
    name = 'Mario'
    children = ['Oliwia', 'Szymon']
    age = 35
    context = {
        'books': books,
        'name': name,
        'children': children,
        'age': age
    }
    for i in context.items():
        print(i)
    return render(request, 'main/test.html', context=context)
