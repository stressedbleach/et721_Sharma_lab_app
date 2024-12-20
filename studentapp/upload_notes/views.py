from django.shortcuts import render, redirect
from .models import Note

def upload_notes(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        file = request.FILES.get('file')
        image = request.FILES.get('image')  # Handle image upload

        # Create and save the Note object
        note = Note(title=title, content=content, file=file, image=image)
        note.save()  # Save the note to the database

        return redirect('upload_notes')  # Redirect after saving

    notes = Note.objects.all()  # Fetch all notes to display
    return render(request, 'blog/upload.html', {'notes': notes})
