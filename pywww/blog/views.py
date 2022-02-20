from django.http import request
from django.http.response import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404, render

from .models import Post


def blog_index(request):
    posts = Post.objects.all()
    print(posts)
    for i in posts:
        print(i.sponsored)
    return render(request, 'blog/index.h.html', {'posts_list': posts})


def post_detail(request, post):
    posts = get_object_or_404(Post, slug=post)
    tags = posts.tags.all()

    return render(request, "blog/post_detail.html", {"post": posts, "tags": tags})
