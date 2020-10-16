from django.http import HttpResponse
from django.shortcuts import render

def ViceVersa(request):
	return render(request, 'ViceVersa.html')