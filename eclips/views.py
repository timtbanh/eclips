from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render_to_response('index.html')

#def index(request):
#	return render(request, "index.html")

def login(request):
	return render(request, "account/login.html")

