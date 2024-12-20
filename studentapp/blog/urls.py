# blog/urls.py
from django.urls import path
from blog.views.blog_posts_views import blog_posts, add_post, post_detail  # Include the post_detail view

urlpatterns = [
    path('', blog_posts, name='blog_posts'),
    path('add/', add_post, name='add_post'),
    path('<int:id>/', post_detail, name='blog_post_detail'),  # URL pattern for post detail
]
