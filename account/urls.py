from django.conf.urls import include, url
from django.contrib import admin
from . import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', v.index, name='index'),
    url(r'^account/signup.html$', v.signup, name='signup'),
    url(r'^account/login.html$', v.login, name='login'),
]

urlpatterns += staticfiles_urlpatterns()


