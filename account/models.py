#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

HOSTEL_CHOICES = (
    ('Alaknanda','Alaknanda'),
)

DEPT_CHOICES = (
    ('Events','Events'),
    )

class UserProfile(models.Model):
    user        = models.ForeignKey(User, unique=True)
    nick        = models.CharField(max_length = 20, blank = True)
    room_no     = models.CharField(max_length = 5, blank = False, null = False)
    hostel      = models.CharField(max_length = 40, choices = HOSTEL_CHOICES, blank = False, null = False)
    ph_no       = models.CharField(max_length = 15, unique = True, blank = False, null = False)
    is_core_of  = models.CharField(max_length = 40, choices = DEPT_CHOICES, null = True)
    cgpa        = models.FloatField()
    
class Announcement(models.Model):
    """
      Stores announcements that will be displayed in the login screen.
      This model objects will be handled from the django admin site.
    """
    message     = models.TextField()
    timestamp   = models.TimeField(auto_now = True, editable = False)


