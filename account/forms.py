from django import forms

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
    
class BarberCreationForm(forms.Form):
    # what else should be included here? PRICES, SCHEDULE, WALKIN, DRIVE TO
    description = TAModelForm
    skills = TAModelForm
    walkin = forms.CharField()
    schedule = TAModelForm
    
class TAModelForm( forms.ModelForm ):
    # TA means Textarea
    descr = forms.CharField( widget=forms.Textarea )
    class Meta:
        model = Textarea