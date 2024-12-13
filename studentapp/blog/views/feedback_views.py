from django.shortcuts import render, redirect
from ..models.feedback_models import Feedback
from ..forms.feedback_forms import FeedbackForm

def feedback_form(request, post_id):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()  # Save the feedback to the database
            return redirect('post_detail', id=post_id)  # Redirect after successful submission
    else:
        form = FeedbackForm()
    return render(request, 'blog/feedback_form.html', {'form': form})
