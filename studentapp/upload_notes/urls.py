from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_notes, name='upload_notes'),  # Upload notes view
]
