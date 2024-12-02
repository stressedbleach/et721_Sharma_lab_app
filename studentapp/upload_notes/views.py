from django.shortcuts import render
from .models import Note

def upload_notes(request):
    notes = Note.objects.all()
    return render(request, 'upload_notes/notes_list.html', {'notes': notes})
