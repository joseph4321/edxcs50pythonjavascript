from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	return HttpResponse("Hello, World")

def joseph(request):
	return HttpResponse("Hello, Joseph")

def greet(request, name):
	return HttpResponse("Hello, " + name)
