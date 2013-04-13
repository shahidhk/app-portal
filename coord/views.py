#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.context_processors import csrf
from django.shortcuts import *
from django import forms
from django.forms.formsets import formset_factory
from coord.forms import *
from coord.models import *
from core.models import *

def coord_home(request):
    """
    Can edit profile,logout
    Sees list of sub-departments, submit application, set preference order etc.  

    """
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user = request.user)
        if profile.is_core_of:
            return HttpResponseRedirect(settings.SITE_URL"/core/") 
    else:
        return HttpResponseRedirect(settings.SITE_URL)    
    return render_to_response("/coord/home.html", locals(),context_instance=RequestContext(request))    
    

def application(request, sub_dept_id = 0):
    """
    Displays questions of the sub-department with id = sub_dept_id            
    
    """
    if request.user.is_authenticated:
        questions = Question.objects.filter(subdept.id = sub_dept_id)
        number_of_questions = questions.count()
        #Create as many answer forms as there are questions
        try:
            a = Application.objects.get(user = request.user, subdept.id = sub_dept_id)
            AnswerFormSet = inlineformset_factory(AnswerForm)
            answers = []
            ans = Answer.objects.filter(user = request.user,question.subdept.id = sub_dept_id).order_by(question.id)
            n = 0
            for a in ans:
                if a.question == questions[n]
                    answers.append(a)
                else:
                    answers.append(' ')
                n=n+1        
            if request.method == 'POST':
                forms = AnswerFormSet(request.POST,instance = answers)
                app = ApplicationForm(request.POST, instance = a)
                if forms.is_valid and app.is_valid:
                    try:
                        apppref = Application.objects.get(preference = app.preference)
                        if apppref.id not app.id:
                            return HttpResponse("You already have this preference number")    
                    except:
                        n=0;
                        f = forms.save(commit = false)
                        for f in forms:
                            f.question = questions[n]
                            f.save()
                            app.save()
                            n=n+1
            else:
                forms = AnswerFormSet()
                app = ApplicationForm()
        except:    
            AnswerFormSet = formset_factory(AnswerForm, extra = number_of_questions)
            if request.method == 'POST':
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
                            f.question = questions[n]
                            f.save()
                            app.save()
                            n=n+1
            else:
                forms = AnswerFormSet()
                app = ApplicationForm()
    
        return render_to_response("/coord/application.html", locals(),context_instance=RequestContext(request))                    
