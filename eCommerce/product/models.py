# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
	title=models.CharField(max_length=225)
	description=models.TextField()
	price=models.DecimalField(decimal_places=2,default=39.99,max_digits=10)
	img=models.ImageField(null=True,blank=True)

	def __str__(self):
		return self.title
class Cart(models.Model):
	product=models.ManyToManyField(Product)
	total=models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
	def __unicode__(self):

		return "cart id :%s"%(self.id )

class UserProfile(User):
	phone=models.CharField(max_length=225)
class abc(models.Model):
	phone=models.CharField(max_length=225)
