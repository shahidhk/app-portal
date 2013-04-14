#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from account.views import *
from django.contrib.auth.views import password_change
from django.conf import settings

urlpatterns = patterns('',
    url(r'^password_change/$', password_change,{'post_change_redirect':settings.SITE_URL}),
    url(r'^login/$', 'account.views.login', name='login'),
    url(r'^register/$', 'account.views.register', name='home'),
    url(r'^logout/$', 'account.views.logout', name='logout'),
    url(r'^editprofile/$', 'account.views.editprofile', name='editprofile'),
)

