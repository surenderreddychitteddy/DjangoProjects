# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(User):
	phonenumber=models.CharField(max_length=10)
	empid=models.CharField(max_length=10)
	name=models.CharField(max_length=220)


