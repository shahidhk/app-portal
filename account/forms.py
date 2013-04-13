#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from django import forms
from django.forms.util import ValidationError
from django.contrib.auth.models import User
from account.models import UserProfile

alnum_re    = re.compile(r'^[\w.-]+$')  # regexp. from jamesodo in #django  [a-zA-Z0-9_.]
alphanumric = re.compile(r"[a-zA-Z0-9]+$")


class LoginForm(forms.Form):
    """
        This form is used for login
    """
    username = forms.CharField(help_text = 'Your registered Roll No')
    password = forms.CharField(widget    = forms.PasswordInput, help_text='Your password')


class RegistrationForm(forms.ModelForm):
    """
        This model form is used registration by the aspiring coordinators
    """
    first_name     = forms.CharField(max_length = 30)
    last_name      = forms.CharField(max_length = 30)
    rollno         = forms.CharField(max_length = 8, help_text='Please enter your Roll No.', label='Roll Number')
    email          = forms.EmailField()
    password       = forms.CharField(min_length = 6, max_length = 30, widget = forms.PasswordInput, help_text = 'Passwords need to be atleast 6 characters long.')
    password_again = forms.CharField(min_length = 6, max_length = 30, widget = forms.PasswordInput, help_text = 'Enter the same password that you entered above')

    class Meta:
    
        model = UserProfile
        exclude = ('user')

    def clean_rollno(self):
        if not alphanumric.search(self.cleaned_data['rollno']):
            raise forms.ValidationError(u'Roll No can only contain letters and numbers')
        if User.objects.filter(username = self.cleaned_data['rollno']):
            pass
        else:
            return self.cleaned_data['rollno']
        raise forms.ValidationError('This username is already taken. Please choose another.')

    def clean_email(self):
        if User.objects.filter(email = self.cleaned_data['email']):
            pass
        else:
            return self.cleaned_data['email']
        raise forms.ValidationError('This email address is already taken. Please choose another.')

    def clean_password(self):
        if self.prefix:
            field_name1 = '%s-password' % self.prefix
            field_name2 = '%s-password_again' % self.prefix
        else:
            field_name1 = 'password'
            field_name2 = 'password_again'

        if self.data[field_name1] != '' and self.data[field_name1] != self.data[field_name2]:
            raise forms.ValidationError('The entered passwords do not match.')
        else:
            return self.data[field_name1]

