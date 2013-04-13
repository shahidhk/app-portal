#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
from django import forms
from django.forms.formsets import formset_factory
from account.models import *
from coord.models import *
from core.models import *
from coord.forms import *

def coord_home(request):
    """
    Can edit profile,logout
    Sees list of sub-departments, submit application, set preference order etc.  

    """
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user__id = request.user.id)
            if profile.is_core_of:
                return HttpResponseRedirect(settings.SITE_URL + "core/") 
        except:
            return HttpResponse("Error!")
        if request.method == "POST":
                form = SelectSubDeptForm(request.POST)
    else:
        return HttpResponseRedirect(settings.SITE_URL)
    form = SelectSubDeptForm()    
    return render_to_response("coord/home.html", locals(),context_instance=RequestContext(request))    
    

def application(request, sub_dept_id = 0):
    """
    Displays questions of the sub-department with id = sub_dept_id            
    
    """
    if request.user.is_authenticated:
        qns = Question.objects.filter(subdept__id = sub_dept_id).order_by('id')
        number_of_questions = qns.count()
        #Create as many answer forms as there are questions
        try:
            a = Application.objects.get(user = request.user, subdept__id = sub_dept_id)
            AnswerFormSet = inlineformset_factory(AnswerForm)
            """
            answers = []
            n=0
            for ans in a.answers.objects.all().order_by(question.id):
                if ans.question == questions[n]
                    answers.append(ans)
                else:
                    answers.append(' ')
                n=n+1     
            """   
            if request.method == 'POST':
                forms = AnswerFormSet(request.POST,instance = a.answers.objects.all())
                app = ApplicationForm(request.POST, instance = a)
                if forms.is_valid and app.is_valid:
                    try:
                        app_pref = Application.objects.get(preference = app.preference)
                        if app_pref.id != app.id:
                            return HttpResponse("You already have this preference number")    
                    except:
                        n=0;
                        f = forms.save(commit = false)
                        for f in forms:
                            f.question = qns[n]
                            f.save()
                            app.save()
                            n=n+1
            else:
                forms = AnswerFormSet()
                app = ApplicationForm()
        except:    
            AnswerFormSet = formset_factory(AnswerForm, extra = number_of_questions)
            if request.method == 'POST':
                print 'blah'
                forms = AnswerFormSet(request.POST)
                app = ApplicationForm(request.POST)
                if forms.is_valid and app.is_valid:
                    try:
                        a = Application.objects.get(preference = app.preference)  
                        return HttpResponse("You already have this preference number")
                    except:  
                        n=0;
                        f = forms.save(commit = false)
                        for f in forms:
                            f.question = qns[n]
                            f.save()
                            app.save()
                            n=n+1
            else:
                forms = AnswerFormSet()
                app = ApplicationForm()
        zipped = zip(qns,forms)
        return render_to_response("coord/application.html", locals(),context_instance=RequestContext(request))                    
