#!/usr/bin/python
# -*- coding: utf-8 -*-

from django                     import forms
from django.contrib.auth.models import User
from coord.models               import *
from core.models                import *

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

class SubDeptForm(forms.ModelForm):
    name = forms.ChoiceField(queryset=SubDept.objects.all())
    class Meta:
        model = SubDept
        fields = {'name'}
        

class CredentialsForm(forms.ModelForm):
    class Meta:
        model = Credentials
        widgets = {'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
        
class ReferencesForm(forms.ModelForm):
    class Meta:
        model = References
        widgets = {'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}

