from django.shortcuts import render, redirect
from .models import Task

def task_list(request):
    if request.method == 'POST':
        task_text = request.POST.get('task')  # Get the task from the form
        if task_text:  # Ensure that the task_text is not empty
            Task.objects.create(task=task_text)  # Save the new task to the database
    
    # Fetch all tasks from the database to display
    tasks = Task.objects.all()
    
    return render(request, 'blog/task_list.html', {'tasks': tasks})
