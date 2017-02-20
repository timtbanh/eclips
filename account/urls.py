from django.conf.urls import include, url
from django.contrib import admin
from eclips import views as v
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^$', v.index, name='index'),
    url(r'^login/$', v.login, name='login'),
]

urlpatterns += staticfiles_urlpatterns()


'''
urlpatterns = patterns('',
    

    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'accounts/login.html'}
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/'}
    ),
)
'''