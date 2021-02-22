from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(render):
	if not request.user.is_authenticated:
		return HttpResponseRedirect(reverse("login"))
	
def login_view(render):
	return render(request, "users/login.html")

def logout_view(render):
	pass
