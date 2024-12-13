from django.shortcuts import render

# Example for home view
def home(request):
    return render(request, 'blog/index.html')

# Example for post_detail view
def post_detail(request, id):
    return render(request, 'blog/post_detail.html', {'id': id})
