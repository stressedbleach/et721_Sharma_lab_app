from django.db import models
from .post_models import Post 

class Feedback(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='feedback')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
