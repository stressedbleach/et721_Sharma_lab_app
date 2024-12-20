from django.shortcuts import render, redirect
from ..models.post_models import Post

def blog_posts(request):
    # Fetch all posts from the database
    posts = Post.objects.all()
    # Render the blog_posts.html template and pass the posts to it
    return render(request, 'blog/blog_posts.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        # Get data from the form
        title = request.POST['title']
        details = request.POST['details']
        content = request.POST['content']

        # Create a new post
        Post.objects.create(title=title, details=details, content=content)

        # Redirect to the blog posts page after saving
        return redirect('blog_posts')

    # If GET request, just render the add post form
    return render(request, 'blog/add_post.html')

def post_detail(request, id):
    # Fetch the specific post based on its ID
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {'post': post})
