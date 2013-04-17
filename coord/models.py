#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from account.models import DEPT_CHOICES
from core.models import SubDept, Question

PREF_CHOICES =(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        )
STATUS_CHOICES=(
        ('accepted','Accepted'),
        ('pending','Pending'),
        ('rejected','Rejected'),
        )

class Answer(models.Model):
    """
    Stores a textfield answer to each question.
    """
    question = models.ForeignKey(Question, null = True)
    answer   = models.TextField(default = 'Enter Answer here',blank = True)

    def __unicode__(self):
        return "%s..." % str(self.answer[:10])

    def get_full_content(self):
        return str(self.answer)

class Credential(models.Model):
    """
    Stores credentials of the user.

    TODO:
    Add a key to user if you want credential
    details specifically.
    """
    content = models.TextField()

    def __unicode__(self):
        return "%s..." % str(self.content[:10])

    def get_full_content(self):
        return str(self.content)

class Reference(models.Model):
    """
    Stores references given by the user.

    TODO:
    Add a key if you want user-specific
    references
    """
    content = models.TextField()

    def __unicode__(self):
        return "%s..." % str(self.content[:10])

    def get_full_content(self):
        return str(self.content)

class Application(models.Model):
    """
    Stores each application made by
    aspiring coords with keys to
    credentials and references.
    """
    user        = models.ForeignKey(User)
    subdept     = models.ForeignKey(SubDept)
    answers     = models.ManyToManyField(Answer)
    preference  = models.IntegerField(default=1)
    credentials = models.ForeignKey(Credential)
    references  = models.ForeignKey(Reference)
    lockstatus  = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now=True, editable=False)
    rank    = models.IntegerField(default=-1) # This field determines if the core has selected the application and the priority assigned
    status = models.CharField(max_length='10',choices=STATUS_CHOICES,default='pending')
    
    def pass_cgpa(self):
        if self.user.get_profile().cgpa >7.0:
            return True
        else:
            return False
