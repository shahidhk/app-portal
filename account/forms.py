#!/usr/bin/python
# -*- coding: utf-8 -*-

from django import forms
from django.forms.util import ValidationError
from django.contrib.auth.models import User

class LoginForm(forms.Form):

    username = forms.CharField(help_text='Your registered Roll No')
    password = forms.CharField(widget=forms.PasswordInput, help_text='Your password')

