from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignupForm, EditClientForm, BarberInfoForm
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

#   helper function to save all client info in one object
def getBarber(barberObj):
    return {
        'firstName': barberObj.firstName,
        'lastName': barberObj.lastName,
        'email': barberObj.email,
        'password': barberObj.password,
        'phone': barberObj.phone,
        'address': barberObj.address,
        'description': barberObj.description,
        'price': barberObj.price,
        'walkin': barberObj.walkin,
        'schedule': barberObj.schedule,
        'avgRating': barberObj.avgRating,
        'profilePic': barberObj.profilePic
    }

def index(request):
    return render_to_response('index.html')

# conrtroller for crateing a new account
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
                outURL = '{0}/{1}'.format(email,'barbercreation.html')
                return HttpResponseRedirect(outURL)

            elif(userType == 'selectClient'):
                clientObj = Client(
                    firstName=firstName,
                    lastName=lastName,
                    email=email,
                    password=password,
                    phone=phone,
                    address=address)
                clientObj.save()    #save this new client to the database
                outURL = '{0}/{1}'.format(email,'clienthome.html')
                return HttpResponseRedirect(outURL)
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
    
    if (request.method == 'POST'):
        form = BarberInfoForm(data=request.POST)   # instance of BarberCreationForm
        print('form is ' + str(form.is_valid()))
        if (form.is_valid()):
            #save the information in the form to variables
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            walkin = form.cleaned_data['walkin']
            schedule = form.cleaned_data['schedule']
        
            # .filter returns a queryset object
            barberRow = Barber.objects.filter(email=barberEmail)
            if (barberRow.exists()):
                barberRow.update(
                    description=description,
                    price=price,
                    walkin=walkin,
                    schedule=schedule)

                outURL = 'barberhome.html'

                return HttpResponseRedirect(outURL)
    else:
        form = BarberInfoForm()
        
    return render(request, "account/barbercreation.html", {'form': form})

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

def editclient(request, clientEmail):
    clientObj = Client.objects.get(email=clientEmail)
    
    data = {
        'email':clientObj.email,
        'phone':clientObj.phone,
        'address':clientObj.address,
        'description':clientObj.description,
        'profilePic':clientObj.profilePic
    }
    form = EditClientForm(initial = data)
    
    if(request.method=='POST'):
        form = EditClientForm(request.POST, request.FILES)   # instance of EditClientForm
        if (form.is_valid()):
            #save the information in the form to variables
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            description = form.cleaned_data['description']
            profilePic = form.cleaned_data['profilePic']
            
            clientObj.email = email
            clientObj.phone = phone
            clientObj.address = address
            clientObj.description = description
            clientObj.profilePic = profilePic
            clientObj.save()
            return HttpResponseRedirect('clientprofile.html')
    #editclient.html posts to this same page and then this view will redirect
    return render(request, 'account/editclient.html', {'form': form})

def makeappointment(request):
    return render(request, 'account/makeappointment.html')

def fakeclienthome(request):
    return render(request, "account/fakeclienthome.html")
def fakeclientprofile(request):
    return render(request, "account/fakeclientprofile.html")
def fakebarberprofile(request):
    return render(request, "account/fakebarberprofile.html")