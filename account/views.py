#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from account.models import Announcement
from account.forms import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active and not user.is_superuser:
            auth_login(request, user)
            nextURL = request.GET.get('next','')
            if nextURL != '':
                nextURL = nextURL[1:]  # For removing the leading slash from in front of the next parameter
                redirectURL = settings.SITE_URL + nextURL
                return HttpResponseRedirect(redirectURL)
            if user.get_profile().is_core_of:
                return HttpResponseRedirect(settings.SITE_URL + 'core/')
            else:
                return HttpResponseRedirect(settings.SITE_URL + 'coord/')
        invalid_login = True
        login_form = LoginForm()
        return render_to_response('home.html', locals(), context_instance=RequestContext(request))
    else:
      return HttpResponseRedirect('/')

def register(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            data = register_form.cleaned_data
            new_user = User(first_name = data['first_name'], last_name  = data['last_name'],
                            username   = data['rollno'], email = data['email'])
            new_user.set_password(data['password'])
            new_user.is_active = True
            new_user.save()
            new_profile = UserProfile(
                user  = new_user,
                nick  = data['nick'],
                room_no  = data['room_no'],
                hostel  = data['hostel'],
                cgpa  = data['cgpa'],
                ph_no = data['ph_no'],
                )
            new_profile.save()
            registered = True
    else:
        register_form = RegistrationForm()
    return render_to_response('register.html', locals(), context_instance=RequestContext(request))

def logout(request):
    if request.user.is_authenticated():
        auth_logout(request)
        return HttpResponseRedirect(settings.SITE_URL)
    else:
      return HttpResponseRedirect('/')

