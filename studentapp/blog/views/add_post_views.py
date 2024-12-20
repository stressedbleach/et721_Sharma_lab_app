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
