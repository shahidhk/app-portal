from django.conf.urls import patterns, include, url
from account.views import *

urlpatterns = patterns('',
    url(r'^login/', 'account.views.login', name='login'),
    url(r'^register/', 'account.views.register', name='home'),
    url(r'^logout/', 'account.views.logout', name='logout'),
    url(r'^editprofile/', 'account.views.editprofile', name='editprofile'),
)

