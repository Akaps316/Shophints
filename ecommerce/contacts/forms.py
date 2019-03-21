from .models import Feedback
from django import forms





class FeedbackForm(forms.ModelForm):
	name = forms.CharField(label='Name', widget=forms.TextInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'name'}))
	email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Email'}))
	subject = forms.CharField(label='Subject', widget=forms.TextInput(
        attrs={'class': 'form-control my-2', 'placeholder': 'Subject'}))
	message = forms.CharField(label='Message', widget=forms.Textarea(
        attrs={'class': 'form-control my-2', 'placeholder': 'message'}))





	class Meta:
		model = Feedback
		fields = '__all__'

    