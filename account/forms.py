from django import forms
from django.forms import DateTimeField
from models import Client


class SignupForm(forms.Form):
    # choices used for the radio button
    CHOICES = [
        ('selectBarber', 'I am a Barber'),
        ('selectClient', 'I am a Client')]

    userType = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    phone = forms.CharField()
    

class AppointmentForm(forms.Form):
    # choices for location of the barber
    CHOICES = [
        ('selectLocationBarber', "Barber's House"),
        ('selectLocationClient', "Client's House")]
    when = forms.DateTimeField(widget=forms.DateTimeInput())
    address = forms.CharField()
    # barber = forms.ForeignKey(Barber,on_delete=models.CASCADE)
    # client = models.ForeignKey(Client, on_delete=models.CASCADE)

class EditClientForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    address = forms.CharField()
    phone = forms.CharField()

class EditBarberForm(forms.Form):
    description = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    address = forms.CharField()
    phone = forms.CharField()
    price = forms.CharField()
    walkin = forms.CharField()
    schedule = forms.CharField(widget=forms.Textarea)
    profilePic = forms.CharField()
    