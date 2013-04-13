#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.forms import ModelForm
from core.models import *
from coord.models import *
from account.models import *
#from django import form

class QuestionForm(ModelForm):
    """
    Form that allows cores to add
    questions to a specific subdept.
    """
    class Meta:
        model=Question
        exclude=('subdept')

    def __init__(self, *arg, **kwarg):
        super(QuestionForm, self).__init__(*arg, **kwarg)
        self.empty_permitted = False

class SubDeptForm(ModelForm):
    """
    Form that allows adding subdepts.
    """
    class Meta:
        model=SubDept
        exclude=('dept')

    def __init__(self, *arg, **kwarg):
        super(SubDeptForm, self).__init__(*arg, **kwarg)
        self.empty_permitted = False

