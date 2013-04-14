#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings
#from django import forms
from django.forms.formsets import formset_factory
from django.contrib.auth.decorators import login_required

from account.models import *
from core.models import *
from coord.models import *
from coord.forms import *

@login_required
def coord_home(request):
    """
    Can edit profile,logout
    Sees list of sub-departments, submit application, set preference order etc.  

    #TODO: Add is_coord decorator
    """
    profile = UserProfile.objects.get(user__id = request.user.id)
    if request.method == "POST":
        form = SelectSubDeptForm(request.POST)
        if form.is_valid():
            subdept = SubDept.objects.get(name = form.cleaned_data['name'])
            return HttpResponseRedirect(settings.SITE_URL + "coord/application/"+ str(subdept.id)) 
    form = SelectSubDeptForm()    
    return render_to_response("coord/home.html", locals(),context_instance=RequestContext(request))    
    
@login_required
def application(request, sub_dept_id = 0):
    """
    Displays questions of the sub-department with id = sub_dept_id            
    
    """
    qns = Question.objects.filter(subdept__id = sub_dept_id).order_by('id')
    number_of_questions = qns.count()
    app = ApplicationForm()
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
            if forms.is_valid() and app.is_valid():
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
        #AnswerFormSet = formset_factory(AnswerForm, extra = number_of_questions)
        if request.method == 'POST':
            #forms = AnswerFormSet(request.POST)
            #print 'blah'
            app = ApplicationForm(request.POST)
            #if forms.is_valid() and app.is_valid():
            if app.is_valid():
                try:
                    a = Application.objects.get(preference = app.preference)  
                    return HttpResponse("You already have this preference number")
                except:
                    app.save() 
                    """ 
                    n=0;
                    f = forms.save(commit = false)
                    for f in forms:
                        f.question = qns[n]
                        f.save()
                        app.save()
                        n=n+1
                    """
            else:
                #forms = AnswerFormSet()
                app = ApplicationForm()
        #zipped = zip(qns,forms)
        return render_to_response("coord/application.html", locals(),context_instance=RequestContext(request))                    
