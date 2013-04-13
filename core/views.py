# ShaastraWebOps

from django.shortcuts import render_to_response, redirect, HttpResponseRedirect
from django.forms.models import modelformset_factory,inlineformset_factory
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from core.models import *
from coord.models import *
from account.models import *
from core.forms import *

#@login_required
def core_dashboard(request):
    """
    Displays the default dashboard of the core.

    TODO:
    Add is_core decorator
    """
    #subdepts=request.user.get_profile().CoreSubDepts()
    displaydict={}
    #displaydict['subdepts']=subdepts
    return render_to_response("core.html",locals())

def questions(request,subdept=None):
    QuestionFormset = modelformset_factory(Question, form=QuestionForm, extra=5)
    if request.method == 'POST':
        questionformset=QuestionFormset(request.POST)
        if questionformset.is_valid():
            for questionform in questionformset:
                question=questionform.save(commit=False)
                question.subdept=subdept
                question.save()
    questionformset = QuestionFormset(queryset=Question.objects.none())
    return render_to_response("questions.html", locals())


def departments(request):
    SubdeptFormset = modelformset_factory(SubDept, form=SubDeptForm, extra=5)
    if request.method == 'POST':
        subdeptformset=SubdeptFormset(request.POST)
        if subdeptformset.is_valid():
            for subdeptform in subdeptformset:
                subdept=subdeptform.save(commit=False)
                subdept.dept=request.user.get_profile.is_core_of
                subdept.save()
    subdeptformset = SubdeptFormset(queryset=Subdept.objects.none())
    return render_to_response("subdepts.html", locals())

def submissions(request,subdept=None):
    apps = Application.objects.filter(subdept=subdept)
    return render_to_response("submissions.html",locals())

def applicants(request,subdept=None):
    apps = Application.objects.filter(subdept=subdept)
    applicants = [app.user for app in apps]
    return render_to_response("applicants.html",locals())

