# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

 
# Create your models here.
class todolist(models.Model):
	Status_type=[('Inprogress','In progress'),('completed','completed'),('pending','pending')]

	Title=models.CharField(max_length=20)
	Description=models.CharField(max_length=225)
	datetime=models.DateTimeField(auto_now_add=True,auto_now=False)
	Status=models.CharField(max_length=250,choices=Status_type)
	Createdat=models.ForeignKey(User)
	Modifiedat=models.DateTimeField(auto_now_add=False,auto_now=True)

	class Meta:
		db_table="todolist"

	def __str__(self):
		return self.Title



