from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.



from django.contrib import messages
from .forms import FeedbackForm





def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('feedback')
    else:
        f = FeedbackForm()
    return render(request, 'contacts/feedback.html', {'form': f})