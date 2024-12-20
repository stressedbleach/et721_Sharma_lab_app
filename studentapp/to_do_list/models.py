from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=255)  # Ensure this field exists
    created_at = models.DateTimeField(auto_now_add=True)  # This can be auto-generated

    def __str__(self):
        return self.task
