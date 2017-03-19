from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.images import ImageFile
from django.core.files.base import File
from .models import Barber, Gallery, Client, Appointment, Review
from .forms import SignupForm, EditClientForm, EditBarberForm, LoginForm, AppointmentForm
import hashlib   # password hasher
from datetime import datetime


def update_filename(instance, filename):
    path = "upload/path/"
    format = instance.userid + instance.file_extension
    return os.path.join(path, format)

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
        'profilePic': barberObj.profilePic,
        'skills': barberObj.skills
        
    }

#   helper function to format all appointments in one object
def getAppointment(apptObj):
    return {
        'pk': apptObj.pk,
        'when': apptObj.when,
        'address': apptObj.address,
        'barber': getBarber(apptObj.barber),
        'client': getClient(apptObj.client),
        'isCompleted': apptObj.isCompleted
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
                request.session['email'] = email
                outURL = '{0}/{1}'.format(email,'barberhome.html', {'email': email})
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
                request.session['email'] = email
                outURL = '{0}/{1}'.format(email,'clienthome.html', {'email': email})
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

def help(request):
    # a user is logged in
    if (request.session.has_key('email')):
        email = request.session['email']
        return render(request, "account/help2.html")

    # no users are logged in
    return render(request, "account/help.html")

def barberhome(request, barberEmail):
    if (request.session.has_key('email')):
        email = request.session['email']
        try:
            barberObj = Barber.objects.get(email=barberEmail)
            returnBarber = getBarber(barberObj)
            
            #get list of appointments
            apptQuery = Appointment.objects.filter(barber=barberObj)
            apptList = [getAppointment(singleAppt) for singleAppt in apptQuery]
            return render(request, 'account/barberhome.html', {'barber': returnBarber, 'apptList':apptList})
        except ObjectDoesNotExist:
            pass
    return HttpResponseRedirect('../login.html')

def clienthome(request, clientEmail):
    if (request.session.has_key('email')):
        email = request.session['email']
        try:
            clientObj = Client.objects.get(email=clientEmail)
            returnClient = getClient(clientObj)

            # get a list of appointments associated with this client
            apptQuery = Appointment.objects.filter(client=clientObj)
            apptList = [getAppointment(singleAppt) for singleAppt in apptQuery]
            return render(request, 'account/clienthome.html', 
                          {'client': returnClient,
                            'apptList': apptList} )

        except ObjectDoesNotExist:
            pass
    return HttpResponseRedirect('../login.html')

# TODO
def barberprofile(request, barberEmail):
    barberObj = Barber.objects.get(email=barberEmail)
    returnGallery = barberObj.gallery_set.all()
    returnBarber = getBarber(barberObj)
    return render(request, "account/barberprofile.html", {'barber': returnBarber, 'gallery': returnGallery})

# def barberprofile(request, barberEmail):
#     return render(request, "account/barberprofile.html")

# TODO
def clientprofile(request, clientEmail):
    # filter through the client table by matching emails
    clientObj = Client.objects.get(email=clientEmail)
    returnClient = getClient(clientObj)
    # send the information about the particular client with matching
    # email to clientprofile.html
    return render(request, "account/clientprofile.html", {'client': returnClient})

def editclient(request, clientEmail):
    if (request.session.has_key('email')):
        email = request.session['email']
        try:
            clientObj = Client.objects.get(email=clientEmail)
            data = {
                'phone':clientObj.phone,
                'address':clientObj.address,
                'description':clientObj.description
            }

            form = EditClientForm(data)
        
            if(request.method=='POST'):
                form = EditClientForm(request.POST, request.FILES)   # instance of EditClientForm
                if (form.is_valid()):
                    #save the information in the form to variables
                    phone = form.cleaned_data['phone']
                    address = form.cleaned_data['address']
                    description = form.cleaned_data['description']

                    try:
                        clientObj.profilePic = request.FILES['profilePic']
                    except MultiValueDictKeyError:
                        pass
                    clientObj.phone = phone
                    clientObj.address = address
                    clientObj.description = description
                    clientObj.save()
                    
                    return HttpResponseRedirect('clientprofile.html')

            else:
                form = EditClientForm(initial = data)
            return render(request, 'account/editclient.html', {'form': form})
        except ObjectDoesNotExist:
            pass
    return HttpResponseRedirect('../login.html')

def editbarber(request, barberEmail):
    if (request.session.has_key('email')):
        email = request.session['email']
        try:
            barberObj = Barber.objects.get(email=barberEmail)
            data = {
                'phone':barberObj.phone,
                'address':barberObj.address,
                'description':barberObj.description,
                'price':barberObj.price,
                'walkin':barberObj.walkin,
                'schedule':barberObj.schedule,
                'skills':barberObj.skills
            }
            form = EditBarberForm(initial = data)
        
            if(request.method=='POST'):
                form = EditBarberForm(request.POST, request.FILES)   # instance of EditBarberForm
                if (form.is_valid()):
                    #save the information in the form to variables
                    phone = form.cleaned_data['phone']
                    address = form.cleaned_data['address']
                    description = form.cleaned_data['description']
                    price = form.cleaned_data['price']
                    walkin = form.cleaned_data['walkin']
                    schedule = form.cleaned_data['schedule']
                    skills = form.cleaned_data['skills']
                    try:
                        barberObj.profilePic =request.FILES['profilePic']
                    except MultiValueDictKeyError:
                        pass
                    try:
                        galleryObj = Gallery(barber = barberObj, gallery = request.FILES['gallery'])
                        galleryObj.save();
                    except MultiValueDictKeyError:
                        pass
                    barberObj.phone = phone
                    barberObj.address = address
                    barberObj.description = description
                    barberObj.price = price
                    barberObj.walkin = walkin
                    barberObj.schedule = schedule
                    barberObj.skills = skills
                    barberObj.save();
                    
                    return HttpResponseRedirect('barberprofile.html')

            return render(request, 'account/editbarber.html', {'form': form})

        except ObjectDoesNotExist:
            pass
    return HttpResponseRedirect('../login.html')

    #editclient.html posts to this same page and then this view will redirect
    # return render(request, 'account/editbarber.html', {'form': form})

def findbarber(request, clientEmail):
    if (request.session.has_key('email')):
        email = request.session['email']
        barber_array = Barber.objects.all()
        try:
            clientObj = Client.objects.get(email=clientEmail)
            barberList = Barber.objects.all()
            
            
            return render(request, 'account/findbarber.html',{'barberList': barberList})
        except ObjectDoesNotExist:
            pass
    return HttpResponseRedirect('../login.html')

def makeappointment(request, barberEmail):
    if (request.session.has_key('email')):
        clientEmail = request.session['email']
        print(clientEmail)
        clientObj = Client.objects.get(email=clientEmail)

        barberObj = Barber.objects.get(email=barberEmail)
        if (request.method == 'POST'):
            form = AppointmentForm(data=request.POST)
            print("form is " + str(form.is_valid()))
            if(form.is_valid()):

                # get time
                dateTimeString = form.cleaned_data['when']
                # 03/16/2017 4:36 PM output
                dateTimeObj = datetime.strptime(dateTimeString, '%m/%d/%Y %I:%M %p')

                # get address from radio button
                address="undecided"
                location = form.cleaned_data['addressChoice']
                if(location == "selectLocationBarber"):
                    if(barberObj.address):
                        address = barberObj.address
                else:
                    if(barberObj.address):
                        address = clientObj.address

                # save new appointment into model
                newAppt = Appointment(when=dateTimeObj, address=address, barber=barberObj, client=clientObj)
                newAppt.save()
                outURL = '../{0}/clienthome.html'.format(clientEmail)
                return HttpResponseRedirect(outURL)
        else:
            # empty form if form is not valid
            form = AppointmentForm()
        return render(request, 'account/makeappointment.html',{'form': form})
    #if fail to have session redirect to login
    return HttpResponseRedirect('../../login.html')

def cancelappointment(request, apptReviewID):
        clientEmail = request.session['email']
        apptObj = Appointment.objects.get(pk=apptReviewID)
        apptObj.delete()
        outURL = '../{0}/clienthome.html'.format(clientEmail)
        return HttpResponseRedirect(outURL)
    

