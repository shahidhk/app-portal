#!/usr/bin/python
# -*- coding: utf-8 -*-

from django                     import forms
from django.contrib.auth.models import User
from coord.models               import *
from core.models                import *
from chosen                     import forms as chosenforms

class AnswerForm(forms.ModelForm):
    class Meta:
        model   = Answer
        fields  = {'answer'}
        widgets = {'answer': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
        
class ApplicationForm(forms.ModelForm):
    #preference = chosenforms.ChosenModelChoiceField(queryset=SubDept.objects.get_ids())
    credentials = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
    references = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
    class Meta:
        model = Application
        fields = {'preference','subdept','user',}
        widgets = {'subdept': forms.HiddenInput(),
                   'user'   : forms.HiddenInput(),}
    
    def clean_preference(self):
        """
            This function validates whether the preference number is valid
        """
        
        apps = Application.objects.filter(user = self.cleaned_data['user'], preference = self.cleaned_data['preference'])
        if len(apps):
            for a in apps:
                if a.subdept == self.cleaned_data['subdept']:
                    return self.cleaned_data['preference']
                else:
                    pass    
            raise forms.ValidationError('This preference is already used')
        else:        
            return self.cleaned_data['preference']
    
    
class SelectSubDeptForm(forms.ModelForm):
    name = chosenforms.ChosenModelChoiceField(queryset=SubDept.objects.all().order_by('dept'))
    class Meta:
        model  = SubDept
        fields = {'name'}
        

class CredentialsForm(forms.ModelForm):
    class Meta:
        model   = Credential
        widgets = {'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}
        
class ReferencesForm(forms.ModelForm):
    class Meta:
        model   = Reference
        widgets = {'content': forms.Textarea(attrs={'cols': 80, 'rows': 20}),}

class AppUploadForm(forms.ModelForm):
    # credentials = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
    # references = forms.CharField(widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
    class Meta:
        model = Application
        fields = {'preference','subdept','user', 'app_file'}
        widgets = {'subdept': forms.HiddenInput(),
                   'user'   : forms.HiddenInput(),}