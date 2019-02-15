# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BloodGroup(models.Model):
	blood_group=models.CharField(max_length=250,)

class DonarRegistation(User):
	# b_type=[('O+VE','O+VE'),('O-VE','O-VE'),('A+VE','A+VE'),('A-VE','A-VE'),('B+VE','B+VE'),('AB+VE','AB+VE'),
	# 			('AB-VE','AB-VE'),('B-VE','B-VE')]
	# blood_id=models.ForeignKey(BloodGroup) 
	name=models.CharField(max_length=250)
	addrees=models.CharField(max_length=250)
	cell_no=models.CharField(max_length=250)
	blood_group=models.CharField(max_length=250)		

	# pic=models.FileField()

