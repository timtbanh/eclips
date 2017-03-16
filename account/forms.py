from django import forms
from django.forms import DateTimeField
from models import Client


class SignupForm(forms.Form):
    # choices used for the radio button
    CHOICES = [
        ('selectBarber', 'I am a Barber'),
        ('selectClient', 'I am a Client')]

    userType = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    firstName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Joe', 'size': 40}))
    lastName = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Doe', 'size': 40}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'name@example.com', 'size': 40}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '123 Street, San Diego, CA 92122', 'size': 40}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'size': 40}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '(800) 123-4567', 'size': 40}))

class LoginForm(forms.Form):
    # coices used for the radio button
    CHOICES = [
        ('selectBarber', 'Barber'),
        ('selectClient', 'Client')]

    userType = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'name@example.com', 'size': 40}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'size': 40}))
    

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
    