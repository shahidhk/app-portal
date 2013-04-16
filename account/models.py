#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from core.models import *


HOSTEL_CHOICES = (
    ('Alaknanda','Alaknanda'),
    ('Saras','Saras'),
    ('Jamuna','Jamuna'),
    ('Sharav','Sharav'),
)

DEPT_CHOICES = (
    ('Events','Events'),
    ('Finance','Finance'),
    ('Design','Design'),
)
class UserProfile(models.Model):
    """
        Stores the Profile details of the Users (both Coordinators and Cores).
    """
    user        = models.ForeignKey(User, unique=True)
    nick        = models.CharField(max_length = 20, blank = True)
    room_no     = models.CharField(max_length = 5, blank = False, null = False)
    hostel      = models.CharField(max_length = 40, choices = HOSTEL_CHOICES, blank = False, null = False)
    ph_no       = models.CharField(max_length = 15, unique = True, blank = False, null = False)
    is_core_of  = models.CharField(max_length = 40, choices = DEPT_CHOICES, null = True, blank = True)
    cgpa        = models.FloatField()

    def CoreSubDepts(self):
        if self.is_core_of is '':
            return False
        else:
          pass
          #return SubDept.objects.filter(dept=is_core_of)
    
    def __unicode__(self):
        return str(self.user.username)

class Announcement(models.Model):
    """
      Stores announcements that will be displayed in the login screen.
      This model objects will be handled from the django admin site.
    """
    message     = models.TextField()
    timestamp   = models.TimeField(auto_now = True, editable = False)
    
    def __unicode__(self):
        return self.    message

