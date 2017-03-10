from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignupForm
from .models import Barber, Client, Appointment, Review
import hashlib   # password hasher

#   helper function to save all client info in one object
def getClient(clientObj):
    return {
        'firstName': clientObj.firstName,
        'lastName': clientObj.lastName,
        'email': clientObj.email,
        'password': clientObj.password,
        'phone': clientObj.phone,
        'address': clientObj.address,
        'description': clientObj.description,
        'avgRating': clientObj.avgRating,
        'profilePic': clientObj.profilePic
    }

def index(request):
    return render_to_response('index.html')

def signup(request):
    if (request.method == 'POST'):
        form = SignupForm(data=request.POST)   # instance of signupForm

        if (form.is_valid()):
            # encrypt the password so we can't just read what it is
            pwdEncrypt = hashlib.sha224(form.cleaned_data['password']).hexdigest()

            #save the information in the form to variables
            userType = form.cleaned_data['userType']
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address= form.cleaned_data['address']
            password = pwdEncrypt

            #save info either to Barber or Client model
            if (userType == 'selectBarber'):
                barberObj = Barber(
                    firstName=firstName,
                    lastName=lastName,
                    email=email,
                    password=password,
                    phone=phone
                    address=address)
                barberObj.save()    #save to database this new barber
                return HttpResponseRedirect('barbercreation.html')
            elif(userType == 'selectClient'):
                clientObj = Client(
                    firstName=firstName,
                    lastName=lastName,
                    email=email,
                    password=password,
                    phone=phone
                    address=address)
                clientObj.save()    #save this new client to the database
                return HttpResponseRedirect('clienthome.html')
    else:
        form = SignupForm()
    #signup.html posts to this same page and then this view will redirect
    return render(request, 'account/signup.html', {'form': form})

def login(request):
    return render(request, "account/login.html")

def help(request):
    return render(request, "account/help.html")

def barberhome(request):
    return render(request, "account/barberhome.html")

def barbercreation(request):
    return render(request, "account/barbercreation.html")

def clientcreation(request):
    return render(request, "account/clientcreation.html")

def clienthome(request, clientEmail):
    #filter through the client table by matching emails
    clientObj = Client.objects.get(email=clientEmail)
    returnClient = getClient(clientObj)
    # send the information about the particular client with matching
    # email to clienthome.html
    return render(request, "account/clienthome.html", {'client': returnClient})

def barberprofile(request):
    return render(request, "account/barberprofile.html")