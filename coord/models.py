#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from account.models import DEPT_CHOICES
from core.models import SubDept, Question

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
    answer   = models.TextField(blank = True)

    def __unicode__(self):
        return u'%s' % (self.answer)
    
    def get_short_content(self):
        return u'%s...' % (self.answer[:10])
        

class Credential(models.Model):
    """
    Stores credentials of the user.

    TODO:
    Add a key to user if you want credential
    details specifically.
    """
    content = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s'% (self.content)
        
    def get_short_content(self):
        return u'%s...' % (self.content[:10])
        

class Reference(models.Model):
    """
    Stores references given by the user.

    TODO:
    Add a key if you want user-specific
    references
    """
    content = models.TextField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.content)
        
    def get_short_content(self):
        return u'%s...' % (self.content[:10])
        

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
    credentials = models.ForeignKey(Credential, blank=True, null=True)
    references  = models.ForeignKey(Reference, blank=True, null=True)
    lockstatus  = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now=True, editable=False)
    rank    = models.IntegerField(default=-1) # This field determines if the core has selected the application and the priority assigned
    status = models.CharField(max_length='10',choices=STATUS_CHOICES,default='pending')
    app_file = models.FileField(upload_to="apps", blank=True, null=True)

    def pass_cgpa(self):
        if self.user.get_profile().cgpa >7.0:
            return True
        else:
            return False