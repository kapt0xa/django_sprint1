from django.shortcuts import render
from pathlib import Path


def index(request):
    return render(request, 'blog/index.html')

def post_detail(request):
    return render(request, 'blog/post_detail.html')

def category_posts(request):
    return render(request, 'blog/category_posts.html')
