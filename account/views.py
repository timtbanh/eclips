from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignupForm, EditClientForm, EditBarberForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
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
    try:
        del request.session['email']
    except:
        pass
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
                outURL = '{0}/{1}'.format(email,'barberhome.html')
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
    if(request.session.has_key('email')):
        email = request.session['email']
        try:
            barberObj = Barber.objects.get(email=email)
            returnBarber = getBarber(barberObj)
            outURL = '{0}/{1}'.format(email,'barberhome.html')
            return HttpResponseRedirect(outURL, {'email': email})
        except ObjectDoesNotExist:
            pass

        try:
            clientObj = Client.objects.get(email=email)
            returnClient = getClient(clientObj)
            outURL = '{0}/{1}'.format(email,'clienthome.html', {'email': email})
            return HttpResponseRedirect(outURL)
        except ObjectDoesNotExist:
            pass

    else:
        if (request.method == 'POST'):
            form = LoginForm(request.POST)

            if (form .is_valid()):
                pwdEncrypt = hashlib.sha224(form.cleaned_data['password']).hexdigest()
                userType = form.cleaned_data['userType']
                email = form.cleaned_data['email']
                password = pwdEncrypt

                if (userType == 'selectBarber'):
                    try:
                        barberObj = Barber.objects.get(email=email)
                        returnBarber = getBarber(barberObj)
                        if (password == barberObj.password):
                            request.session['email'] = email
                            outURL = '{0}/{1}'.format(email,'barberhome.html')
                            return HttpResponseRedirect(outURL, {'email': email})
                    except ObjectDoesNotExist:
                        pass

                elif (userType == 'selectClient'):
                    try:
                        clientObj = Client.objects.get(email=email)
                        returnClient = getClient(clientObj)
                        if (password == clientObj.password):
                            request.session['email'] = email
                            outURL = '{0}/{1}'.format(email,'clienthome.html', {'email': email})
                            return HttpResponseRedirect(outURL)
                    except ObjectDoesNotExist:
                        pass
        else:
            form = LoginForm()

        return render(request, 'account/login.html', {'form': form})

def formView(request):
    if (request.session.has_key('email')):
        email = request.session['email']
        return render(request, 'account/login.html', {'email': email})
    else:
        return render(request, 'account/login.html', {})

def logout(request, email):
   try:
      del request.session['email']
   except:
      pass
   return HttpResponseRedirect('../../..')

def help(request):
    return render(request, "account/help.html")

def barberhome(request, barberEmail):
    if (request.session.has_key('email')):
        email = request.session['email']
        try:
            barberObj = Barber.objects.get(email=barberEmail)
            returnBarber = getBarber(barberObj)
            return render(request, 'account/barberhome.html', {'barber': returnBarber})
        except ObjectDoesNotExist:
            pass
    return HttpResponseRedirect('../login.html')

def clienthome(request, clientEmail):
    if (request.session.has_key('email')):
        email = request.session['email']
        try:
            clientObj = Client.objects.get(email=clientEmail)
            returnClient = getClient(clientObj)
            return render(request, 'account/clienthome.html', {'client': returnClient})
        except ObjectDoesNotExist:
            pass
    return HttpResponseRedirect('../login.html')

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
        'description':clientObj.description
    }
    form = EditClientForm(initial = data)
    
    if(request.method=='POST'):
        form = EditClientForm(data=request.POST)   # instance of EditClientForm
        if (form.is_valid()):
            #save the information in the form to variables
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            description = form.cleaned_data['description']

            clientObj.email = email
            clientObj.phone = phone
            clientObj.address = address
            clientObj.description = description
            clientObj.save();
            
            return HttpResponseRedirect('clientprofile.html')

    #editclient.html posts to this same page and then this view will redirect
    return render(request, 'account/editclient.html', {'form': form})
def editbarber(request, barberEmail):
    barberObj = Barber.objects.get(email=barberEmail)
    
    data = {
        'email':barberObj.email,
        'phone':barberObj.phone,
        'address':barberObj.address,
        'description':barberObj.description,
        'price':barberObj.price,
        'walkin':barberObj.walkin,
        'schedule':barberObj.schedule,
        'avgRating':barberObj.avgRating,
        'profilePic':barberObj.profilePic
    }
    form = EditBarberForm(initial = data)
    
    if(request.method=='POST'):
        form = EditBarberForm(data=request.POST)   # instance of EditBarberForm
        if (form.is_valid()):
            #save the information in the form to variables
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            walkin = form.cleaned_data['walkin']
            schedule = form.cleaned_data['schedule']
            profilePic = form.cleaned_data['profilePic']

            barberObj.email = email
            barberObj.phone = phone
            barberObj.address = address
            barberObj.description = description
            barberObj.price = price
            barberObj.walkin = walkin
            barberObj.schedule = schedule
            barberObj.profilePic = profilePic
            barberObj.save();
            
            return HttpResponseRedirect('barberprofile.html')

    #editclient.html posts to this same page and then this view will redirect
    return render(request, 'account/editbarber.html', {'form': form})


def makeappointment(request):
    return render(request, 'account/makeappointment.html')

def fakeclienthome(request):
    return render(request, "account/fakeclienthome.html")
def fakeclientprofile(request):
    return render(request, "account/fakeclientprofile.html")
def fakebarberprofile(request):
    return render(request, "account/fakebarberprofile.html")