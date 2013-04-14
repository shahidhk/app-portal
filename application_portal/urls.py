#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/', include('account.urls')),
    url(r'^core/', include('core.urls')),
    url(r'^coord/', include('coord.urls')),
    url(r'^$', 'application_portal.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
)
