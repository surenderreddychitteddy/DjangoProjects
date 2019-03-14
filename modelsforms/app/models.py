# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):
	name=models.CharField(max_length=220)
	phone=models.CharField(max_length=220)
	email=models.EmailField()
	add=models.TextField()
class Userprofile(User):
	phone=models.CharField(max_length=250)
	add=models.TextField()

