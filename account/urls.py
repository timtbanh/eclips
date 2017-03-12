from django.conf.urls import include, url
from django.contrib import admin
from . import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', v.index, name='index'),
    url(r'^account/signup.html$', v.signup, name='signup'),
    url(r'^account/login.html$', v.login, name='login'),
    url(r'^account/help.html$', v.help, name='help'),
    url(r'^account/(?P<barberEmail>.*)/barberhome.html$', v.barberhome, name='barberhome'),
    url(r'^account/(?P<barberEmail>.*)/barbercreation.html$', v.barbercreation, name='barbercreation'),
    url(r'^account/(?P<clientEmail>.*)/clienthome.html$', v.clienthome, name='clienthome'),
    url(r'^account/barberprofile.html$', v.barberprofile, name='barberprofile'),
    url(r'^account/clientprofile.html$', v.clientprofile, name='clientprofile'),
    url(r'^account/(?P<clientEmail>.*)/clientprofile.html$', v.clientprofile, name='clientprofile'),
    url(r'^account/(?P<clientEmail>.*)/editclient.html$', v.editclient, name='editclient'),
]


urlpatterns += staticfiles_urlpatterns()

