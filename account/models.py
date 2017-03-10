from __future__ import unicode_literals

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
    address = models.CharField(max_length=200, null=True)
    skills = models.TextField(max_length=200, null=True)#list all the services being offered and their prices
    walkin = models.CharField(max_length=200, null=True)#walkin, goto customer, either
    schedule = models.TextField(null=True)#display schedule in form of text
    description = models.TextField(null=True) #other wanted information
    avgRating = models.IntegerField(null=True)#averaged Rating
    profilePic = models.CharField(max_length=200, null=True)#link to prof pic
    def __str__(self):
        return 'Barber Name: %s %s' % (self.firstName, self.lastName)

@python_2_unicode_compatible
class Client(models.Model):
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True) #other wanted information
    avgRating = models.IntegerField(null=True)#averaged Rating
    profilePic = models.CharField(max_length=200, null=True)#link to prof pic
    def __str__(self):
        return 'Client Name: %s %s' % (self.firstName, self.lastName)

@python_2_unicode_compatible
class Appointment(models.Model):
    when = models.DateTimeField(default=datetime.now)
    address = models.CharField(max_length=200)
    barber = models.ForeignKey(Barber,on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    isCompleted = models.BooleanField(default=False)#if by date time, then true
    def __str__(self):
        return 'Appointment between: %s & %s @ %s' % (self.barber.firstName, self.client.lastName, self.when)

@python_2_unicode_compatible
class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    appointment = models.ForeignKey(Appointment, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return 'Review of %s' % (self.appointment)