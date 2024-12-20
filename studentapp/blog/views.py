from django.shortcuts import render

def blog_posts(request):
    posts = Post.objects.all()  # Get all posts from the database
    return render(request, 'blog/blog_posts.html', {'posts': posts})  # Pass posts to the template

# Example for post_detail view
def post_detail(request, id):
    return render(request, 'blog/post_detail.html', {'id': id})

def add_post(request):
    # Handle the post creation logic here
    return render(request, 'blog/add_post.html')  # Return a page to add a post