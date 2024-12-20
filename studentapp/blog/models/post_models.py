from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()  # Make sure this field exists
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
