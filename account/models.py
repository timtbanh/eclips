from __future__ import unicode_literals
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime#
        
@python_2_unicode_compatible
class Barber(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    skills = models.TextField(max_length=200, null=True, blank=True)
    price = models.CharField(max_length=200, null=True, blank=True)#the price they charge
    walkin = models.CharField(max_length=200, null=True, blank=True)#walkin, goto customer, either
    schedule = models.TextField(null=True)#display schedule in form of text
    description = models.TextField(null=True) #other wanted information
    avgRating = models.FloatField(null=True)#averaged Rating
    profilePic = models.ImageField(upload_to="barbers", null=True, blank=True)
    def __str__(self):
        return 'Barber Name: %s %s' % (self.firstName, self.lastName)

@python_2_unicode_compatible
class Gallery(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE)
    gallery = models.ImageField(upload_to="barbers/gallery", null=True, blank=True)
    def __str__(self):
        return 'Gallery Picture: %s' % (self.gallery.url)
    
@python_2_unicode_compatible
class Client(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True) #other wanted information
    avgRating = models.FloatField(null=True)#averaged Rating 
    profilePic = models.ImageField(upload_to="clients", null=True, blank=True)
    def __str__(self):
        return 'Client Name: %s %s' % (self.firstName, self.lastName)

@python_2_unicode_compatible
class Appointment(models.Model):
    when = models.DateTimeField(default=datetime.now)
    address = models.CharField(max_length=200)
    barber = models.ForeignKey(Barber,on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return 'Appointment between: %s & %s @ %s' % (self.barber.firstName, self.client.lastName, self.when)

@python_2_unicode_compatible
class Review(models.Model):
    comment = models.TextField()
    writer = models.CharField(max_length=200,null=True, blank=True)
    appointment = models.ForeignKey(Appointment, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return 'Review of %s' % (self.appointment)