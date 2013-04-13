#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from account.models import Announcement
from account.forms import *

def home(request):
    if request.user.is_authenticated():
        userprofile = request.user.get_profile()
        if userprofile.is_core_of:
           return HttpResponseRedirect(settings.SITE_URL + 'core/')
        else:
            return HttpResponseRedirect(settings.SITE_URL + 'coord/')
    announcements = Announcement.objects.all()
    login_form = LoginForm()    
    return render_to_response('home.html', locals(), context_instance = RequestContext(request))

