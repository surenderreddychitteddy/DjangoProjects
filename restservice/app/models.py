# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class school(models.Model):
	name=models.CharField(max_length=220)
	add=models.CharField(max_length=220)
class student(models.Model):
	School=models.ForeignKey(school)
	name=models.CharField(max_length=220)
