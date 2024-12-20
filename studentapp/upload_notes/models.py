from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(upload_to='notes/', null=True, blank=True)
    image = models.ImageField(upload_to='notes/images/', null=True, blank=True)  # Add the image field

    def __str__(self):
        return self.title
