from django.contrib.auth import authenticate, login, get_user_model

from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import ContactForm

def home_page(request):
	context = {
	 "title":"Home Page",
	 "content":"Welcome...",


	}
	if request.user.is_authenticated:
		context["premium_content"] = request.user.username
	return render(request,"home_page.html", context)

def about_page(request):
	context = {
	 "title":"About Page"
	}
	return render(request,"home_page.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
	 "title":"Contact",
	 "form":contact_form
	}
	return render(request,"contact/view.html",context)






