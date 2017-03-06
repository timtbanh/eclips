from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render_to_response('index.html')

def signup(request):
    return render_to_response('account/signup.html')

def login(request):
	return render_to_response("account/login.html")

def help(request):
    return render_to_response("account/help.html")

def barberhome(request):
    return render_to_response("account/barberhome.html")

def barbercreation(request):
    return render_to_response("account/barbercreation.html")

def clientcreation(request):
    return render_to_response("account/clientcreation.html")

def clienthome(request):
    return render_to_response("account/clienthome.html")
def barberprofile(request):
    return render_to_response("account/barberprofile.html")