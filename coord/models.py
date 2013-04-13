#!/usr/bin/python
# -*- coding: utf-8 -*-

# ShaastraWebOps

from django.db import models
from django.contrib.auth.models import User
from account.models import DEPT_CHOICES
from core.models import SubDept, Question

class Answer(models.Model):
    """
    Stores a textfield answer to each question.
    """
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    answer = models.TextField()

class Credential(models.Model):
    """
    Stores credentials of the user.

    TODO:
    Add a key to user if you want credential
    details specifically.
    """
    content = models.TextField()

class Reference(models.Model):
    """
    Stores references given by the user.

    TODO:
    Add a key if you want user-specific
    references
    """
    content = models.TextField()

class Application(models.Model):
    """
    Stores each application made by
    aspiring coords with keys to
    credentials and references.
    """
    user = models.ForeignKey(User)
    subdept = models.ForeignKey(SubDept)
    preference = models.IntegerField(default=1)
    credentials = models.ForeignKey(Credential)
    references = models.ForeignKey(Reference)
    lockstatus = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True, editable=False)

