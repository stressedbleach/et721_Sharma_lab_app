from django.shortcuts import render
from ..models.post_models import Post

def index(request):
    posts = Post.objects.all()  # Fetch all posts
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)  # Fetch a specific post
    return render(request, 'blog/post_detail.html', {'post': post})
