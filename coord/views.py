#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import render_to_response, redirect
from django.conf import settings
#from django import forms
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory,inlineformset_factory
from django.contrib.auth.decorators import login_required, user_passes_test

from account.models import *
from core.models import *
from coord.models import *
from coord.forms import *

@login_required
@user_passes_test(lambda u: not u.get_profile().is_core_of)
def coord_home(request):
    """
    Can edit profile,logout
    Sees list of sub-departments, submit application, set preference order etc.

    #TODO: Add is_coord decorator
    """
    profile = UserProfile.objects.get(user__id = request.user.id)
    try:
        apps = Application.objects.filter(user = request.user).order_by('preference')
    except:
        pass
    if request.method == "POST":
        form = SelectSubDeptForm(request.POST)
        if form.is_valid():
            subdept = SubDept.objects.get(name = form.cleaned_data['name'])
            return redirect('coord.views.application', sub_dept_id=subdept.id)
    form = SelectSubDeptForm()    
    return render_to_response("coord/home.html", locals(),context_instance=RequestContext(request))    
    
@login_required
@user_passes_test(lambda u: not u.get_profile().is_core_of)
def application(request, sub_dept_id = None):
    """
    Displays questions of the sub-department with id = sub_dept_id

    #TODO: Do no accept form if an answer is blank
    """
    subdept = SubDept.objects.get(id = sub_dept_id)
    qns = Question.objects.filter(subdept__id = sub_dept_id).order_by('id')
    number_of_questions = qns.count()
    #Create as many answer forms as there are questions
    try:
        AnswerFormSet = modelformset_factory(Answer, form = AnswerForm)
        a = Application.objects.get(user = request.user, subdept__id = sub_dept_id)
        data = {'preference':a.preference,'references':a.references,'credentials' : a.credentials}
        answers = a.answers.all()
        questions = [ans.question for ans in answers]
        if request.method == 'POST':
            #AnswerFormSet = modelformset_factory(Answer, form = AnswerForm)
            forms = AnswerFormSet(request.POST,queryset = a.answers.all())
            app = ApplicationForm(request.POST,data)
            if forms.is_valid() and app.is_valid():
                try:
                    app_pref = Application.objects.get(preference = app.preference)
                    if app_pref.id != app.id:
                        return HttpResponse("You already have this preference number")    
                except:
                    n=0;
                    forms = forms.save()
                    ref = Reference.objects.get(id = a.references.id)
                    ref.content = app.cleaned_data['references']
                    ref.save()
                    cred = Credential.objects.get(id = a.credentials.id) 
                    cred.content = app.cleaned_data['credentials']
                    cred.save()
                    a.references = ref
                    a.credentials = cred
                    a.preference = app.cleaned_data['preference']
                    a.save()
        else:
            
            app = ApplicationForm(data)  
            forms = AnswerFormSet(queryset = a.answers.all())
    except:    
        AnswerFormSet = modelformset_factory(Answer, form = AnswerForm, extra = number_of_questions)
        if request.method == 'POST':
            forms = AnswerFormSet(request.POST,initial=[{'answer':'default'}])
            app = ApplicationForm(request.POST)
            if forms.is_valid() and app.is_valid():
                temp = app.save(commit = False)
                try:
                    app_pref = Application.objects.get(user = request.user, preference = temp.preference)  
                    return HttpResponse("You already have this preference number")
                except:
                    forms = forms.save(commit = False)
                    
                    ref = Reference(content = app.cleaned_data['references'])
                    ref.save()
                    cred = Credential(content = app.cleaned_data['credentials']) 
                    cred.save()
                    temp.user = request.user
                    temp.references = ref
                    temp.credentials = cred
                    temp.subdept = subdept 
                    temp.save()
                    curr = Application.objects.get(id = temp.id)
                    n = 0
                    for f in forms:
                        f.question = qns[n]
                        n=n+1
                        f.save()
                        ans = Answer.objects.get(id = f.id)                        
                        curr.answers.add(ans)
                        comment = Comments(answer = ans, comment = " ")
                        comment.save()
                    curr.save()
                    appcomment = AppComments(app = curr, comment = " ")
                    appcomment.save()
        else:  
            forms = AnswerFormSet(queryset = Answer.objects.none())
            app = ApplicationForm()
    zipped = zip(qns,forms)
    return render_to_response("coord/application.html", locals(),context_instance=RequestContext(request))                    

