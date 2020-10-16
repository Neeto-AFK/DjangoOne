from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {'copyright':'Mukhametzhan Ibrayev'})

def about(request):
	return HttpResponse('This is about page')

def projects(request):
	return HttpResponse('This is my projects of web development')

def contacts(request):
	return HttpResponse('Just text me')