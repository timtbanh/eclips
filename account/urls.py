from django.conf.urls import include, url
from django.contrib import admin
from . import views as v
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', v.index, name='index'),
    url(r'^account/signup.html$', v.signup, name='signup'),
    url(r'^account/login.html$', v.login, name='login'),
    url(r'^account/help.html$', v.help, name='help'),
    url(r'^account/(?P<barberEmail>.*)/barberhome.html$', v.barberhome, name='barberhome'),
    url(r'^account/(?P<clientEmail>.*)/clienthome.html$', v.clienthome, name='clienthome'),
    url(r'^account/(?P<barberEmail>.*)barberprofile.html$', v.barberprofile, name='barberprofile'),
    url(r'^account/(?P<clientEmail>.*)/clientprofile.html$', v.clientprofile, name='clientprofile'),
    url(r'^account/(?P<clientEmail>.*)/editclient.html$', v.editclient, name='editclient'),
    url(r'^account/(?P<barberEmail>.*)/editbarber.html$', v.editbarber, name='editbarber'),
    url(r'^account/(?P<clientEmail>.*)/findbarber.html$',
    v.findbarber, name='findbarber'),
    
    url(r'account/makeappointment.html$', v.makeappointment, name='makeappointment'),
    url(r'^account/fakeclienthome.html$', v.fakeclienthome, name='fakeclienthome'),
    url(r'^account/fakeclientprofile.html$', v.fakeclientprofile, name='fakeclientprofile'),
    url(r'^account/fakebarberprofile.html$', v.fakebarberprofile, name='fakebarberprofile'),
]   

urlpatterns += staticfiles_urlpatterns()

