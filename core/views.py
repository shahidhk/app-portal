#!/usr/bin/python
# -*- coding: utf-8 -*-

# ShaastraWebOps

from django.shortcuts import render_to_response, redirect, HttpResponseRedirect
from django.forms.models import modelformset_factory,inlineformset_factory
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.template.defaultfilters import slugify

from core.models import *
from coord.models import *
from account.models import *
from core.forms import *

def urlhandler(request):
    return redirect('core.views.core_dashboard',username=request.user)

@login_required
@user_passes_test(lambda u: u.get_profile().is_core_of)
def core_dashboard(request,username=None):
    """
    Displays the default dashboard of the core.

    TODO:
    Add is_core decorator
    """
    user = request.user
    subdepts = SubDept.objects.filter(dept=request.user.get_profile().is_core_of)
    print subdepts
    return render_to_response("cores/core.html",locals())

@login_required
@user_passes_test(lambda u: u.get_profile().is_core_of)
def questions_edit(request,username=None,subdept_id=None,q_id=None):
    """
    Working on this.

    This loads up question instance,
    checks if the owner of that question is trying to edit
    it and allows him to do so.
    """
    question=Question.objects.get(id=q_id)
    if (question.subdept.id == subdept_id):
        qedit=QuestionForm(instance=question)
        if request.method=="POST":
            q=QuestionForm(request.POST)
            q.save()
    return render_to_response('core/edit_q.html',locals())


@login_required
@user_passes_test(lambda u: u.get_profile().is_core_of)
def questions(request,username=None,subdept_id=None):
    """
    Add multiple questions to the application
    questionairre of a particualar SubDept.

    TODO:
    Fucntionality of adding common questions
    to all subdepts under a Dept.
    """
    questions = Question.objects.filter(subdept__pk=subdept_id)
    QuestionFormset = modelformset_factory(Question, form=QuestionForm, extra=5)
    if request.method == 'POST':
        index=0
        questionformset=QuestionFormset(request.POST)
        for questionform in questionformset:
            if questionform.is_valid():
                question=questionform.save(commit=False)
                question.subdept=SubDept.objects.get(pk=subdept_id)
                question.save()
                index+=1
    questionformset = QuestionFormset(queryset=Question.objects.none())
    return render_to_response("cores/questions.html", locals())

@login_required
@user_passes_test(lambda u: u.get_profile().is_core_of)
def subdepartments(request,username=None):
    """
    Add Subdepts to a Dept
    """
    SubdeptFormset = modelformset_factory(SubDept, form=SubDeptForm, extra=3)
    if request.method == 'POST':
        index=0
        subdeptformset=SubdeptFormset(request.POST)
        for subdeptform in subdeptformset:
            if subdeptform.is_valid():
                subdept=subdeptform.save(commit=False)

                subdept.dept=request.user.get_profile().is_core_of
                subdept.save()
                index+=1
    subdeptformset = SubdeptFormset(queryset=SubDept.objects.none())
    return render_to_response("cores/subdepts.html", locals())

@login_required
@user_passes_test(lambda u: u.get_profile().is_core_of)
def submissions(request,username=None,subdept=None):
    """
    Portal to access all submissions
    for a partiicualar subdept.
    """
    if subdept:
        subdept = SubDept.objects.get(name = subdept)
        applications = Application.objects.filter(subdept = subdept)
        answers = [app.answer.all() for app in applications]
    else:
        return redirect('core.views.core_dashboard',username=request.user)
    return render_to_response("submissions.html",locals())


@login_required
@user_passes_test(lambda u: u.get_profile().is_core_of)
def applicants(request,username=None,subdept=None):
    """
    Portal to view details about all applicants
    for a subdept.
    """
    apps = Application.objects.filter(subdept=subdept)
    applicants = [app.user for app in apps]
    return render_to_response("cores/applicants.html",locals())

