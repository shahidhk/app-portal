#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from account.models import DEPT_CHOICES


class SubDept(models.Model):
    """
      Each department under Shaastra has sub-departments.
      Example: Design is a Department whereas Graphic Design, Photography etc are sub-departments

    """
    dept        = models.CharField(max_length = 40, choices = DEPT_CHOICES)
    name        = models.CharField(max_length = 40)
#    impose_cgpa = models.BooleanField(default = True)
#    close_apps  = models.BooleanField(default = False)

    def __unicode__(self):
        return self.name

    def get_full_name(self):
        return "%s | %s " %(self.dept,self.name)

    def __unicode__(self):
        return '%s' % (self.name)

class Question(models.Model):
    """
      Each Sub-department has specific questionnaire. This model is for storing the questions and
      to which sub-department they are meant for.

    """
    subdept  = models.ForeignKey(SubDept)
    question = models.TextField()

    def __unicode__(self):
        return "%s..." % str(self.question[:10])
    
    def get_full_content(self):
        return str(self.question)

from coord.models import Answer, Application

class Comments(models.Model):
    """
    Stores comments written by Cores about an answer in an application.
    This helps the core during the interview.
    """
    answer  = models.ForeignKey(Answer)
    comment = models.TextField()
    
    def __unicode__(self):
        return str(self.comment)

class AppComments(models.Model):
    """
    Stores comments written by Cores about an application in general.
    This serves as a useful feedback to the aspiring coordinator who can view this at the end of selection procedure.
    """
    app     = models.ForeignKey(Application,unique=True)
    comment = models.TextField()
    
    def __unicode__(self):
        return str(self.comment)

