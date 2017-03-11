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
            password = pwdEncrypt
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']

            #save info either to Barber or Client model
            if (userType == 'selectBarber'):
                barberObj = Barber(
                    firstName=firstName,
                    lastName=lastName,
                    email=email,
                    password=password,
                    phone=phone,
                    address=address)
                barberObj.save()    #save to database this new barber
                return HttpResponseRedirect('barbercreation.html')
                #returnBarber=getBarber(barberObj)
                #return render(request, "account/barbercreation.html", {'barber': returnBarber}
            elif(userType == 'selectClient'):
                clientObj = Client(
                    firstName=firstName,
                    lastName=lastName,
                    email=email,
                    password=password,
                    phone=phone,
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

def barberhome(request, barberEmail):
    #filter through the barber table by matching emails
    barberObj = Barber.objects.get(email=barberEmail)
    returnBarber = getBarber(barberObj)
    # send the information about the particular barber with matching
    # email to barberhome.html
    return render(request, "account/barberhome.html", {'barber': returnBarber})

def barbercreation(request, barberEmail):
    barberObj = Barber.objects.get(email=barberEmail)
    returnBarber = getBarber(barberObj)
    
    if (request.method == 'POST'):
        form = BarberCreationForm(data=request.POST)   # instance of BarberCreationForm

        if (form.is_valid()):
            #save the information in the form to variables
            desription = form.cleaned_data['description']
            skills = form.cleaned_data['skills']
            walkin = form.cleaned_data['walkin']
            schedule = form.cleaned_data['schedule']
        
            if (userType == 'selectBarber'):
                barberObj = Barber(
                    description=description,
                    skills=skills,
                    walkin=walkin,
                    schedule=schedule)
                barberObj.save()    #save to database this new barber
                return HttpResponseRedirect('barberhome.html')
    else:
        form = BarberCreationForm()
        
    return render(request, "account/barbercreation.html", {'barber': returnBarber})

def clienthome(request, clientEmail):
    #filter through the client table by matching emails
    clientObj = Client.objects.get(email=clientEmail)
    returnClient = getClient(clientObj)
    # send the information about the particular client with matching
    # email to clienthome.html
    return render(request, "account/clienthome.html", {'client': returnClient})

def barberprofile(request):
    return render(request, "account/barberprofile.html")
def clientprofile(request, clientEmail):
    #filter through the client table by matching emails
    clientObj = Client.objects.get(email=clientEmail)
    returnClient = getClient(clientObj)
    # send the information about the particular client with matching
    # email to clientprofile.html
    return render(request, "account/clientprofile.html", {'client': returnClient})