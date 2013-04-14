#!/usr/bin/python
# -*- coding: utf-8 -*-

from django                     import forms
from django.contrib.auth.models import User
from coord.models               import *
from core.models                import *
from chosen                     import forms as chosenforms

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = {'answer'}
        widgets = {'answer': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
        
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = {'preference','credentials','references'}  
        widgets = {'credentials': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
                    'references': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}      

class SelectSubDeptForm(forms.ModelForm):
    name = chosenforms.ChosenModelChoiceField(queryset=SubDept.objects.all())
    class Meta:
        model = SubDept
        exclude = {'dept'}
        

class CredentialsForm(forms.ModelForm):
    class Meta:
        model = Credential
        widgets = {'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
        
class ReferencesForm(forms.ModelForm):
    class Meta:
        model = Reference
        widgets = {'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}

