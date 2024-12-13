from django.urls import path
from blog.views import post_views, feedback_views  # Correct the import here

urlpatterns = [
    path('', lambda request: render(request, 'blog/index.html'), name='home'),
    path('post/<int:id>/', post_views.post_detail, name='post_detail'),
    path('post/<int:post_id>/feedback/', feedback_views.feedback_form, name='feedback_form'),
]
