#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$','core.views.urlhandler'),
    url(r'^(?P<username>\w+)/questions/(?P<subdept_id>\w+)/','core.views.questions',name='core_questions'),
    url(r'^(?P<username>\w+)/subdepartments/$','core.views.subdepartments',name='core_subdepartments'),
    url(r'^(?P<username>\w+)/dashboard/$', 'core.views.core_dashboard', name='core_home'),
    url(r'^(?P<username>\w+)/submissions/(?P<subdept_id>\w+)/','core.views.submissions',name='core_submissions'),
    url(r'^(?P<username>\w+)/applicants/','core.views.applicants',name='core_applicants'),
)

