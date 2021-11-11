from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Post


def blog_index(request):
    posts = Post.objects.all()
    
    return render(request, 'blog/index.h.html', {'posts': posts})

# def blog_index(request):
#     posts = Post.objects.all()    
#     return HttpResponse('Tu bedom posty')
