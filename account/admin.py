from django.contrib import admin

from .models import Barber, Gallery, Client, Appointment, Review
admin.site.register(Barber)
admin.site.register(Gallery)
admin.site.register(Client)
admin.site.register(Appointment)
admin.site.register(Review)
