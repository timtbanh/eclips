from django.conf.urls import include, url
from django.contrib import admin
from . import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', v.index, name='index'),
    url(r'^account/signup.html$', v.signup, name='signup'),
    url(r'^account/login.html$', v.login, name='login'),
    url(r'^account/help.html$', v.help, name='help'),
    url(r'^account/barberhome.html$', v.barberhome, name='barberhome'),
    url(r'^account/clienthome.html$', v.clienthome, name='clienthome'),
]

urlpatterns += staticfiles_urlpatterns()


