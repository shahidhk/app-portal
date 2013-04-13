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
    #subdepts=request.user.get_profile().isCore()
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
    pass

def submissions(request):
    pass

def applicants(request):
    pass
