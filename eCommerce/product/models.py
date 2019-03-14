# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
	# cake=models.ForegienKeyField(Cake)
	# gift=models.ForegienKeyField(Gift)

	title=models.CharField(max_length=225)
	description=models.TextField()
	price=models.DecimalField(decimal_places=2,default=39.99,max_digits=10)
	img=models.ImageField(null=True,blank=True)

	def __str__(self):
		return self.title
class Catagery(models.Model):
	name=models.CharField(max_length=225)
	def __str__(self):
		return self.name
class Products(models.Model):
	

	weight=models.CharField(max_length=225,null=True,blank=True)
	img=models.ImageField(null=True,blank=True)
	description=models.TextField()
	price=models.DecimalField(decimal_places=2,max_digits=10)
	message=models.CharField(max_length=225,null=True,blank=True)


	def __str__(self):
		return self.description



class Cake(models.Model):
	catagery=models.ForeignKey(Catagery)
	weight=models.CharField(max_length=225)
	img=models.ImageField(null=True,blank=True)
	description=models.TextField()
	price=models.DecimalField(decimal_places=2,max_digits=10)
	message=models.CharField(max_length=225,null=True,blank=True)
	available = models.BooleanField(default=True)



	def __str__(self):
		return self.description

class Gift(models.Model):
	img=models.ImageField(null=True,blank=True)
	description=models.TextField()
	price=models.DecimalField(decimal_places=2,max_digits=10)
	date=models.DateField(null=True,blank=True)


	def __str__(self):
		return self.description
# class Product(models.Model):
# 	cake=models.ForeignKey(Cake)
# 	gift=models.ForeignKey(Gift)
	# cake=models.ForeignKey(Cake)
	# gift=models.ForeignKey(Gift)



class Cart(models.Model):
	cake=models.ManyToManyField(Cake)

	total=models.DecimalField(decimal_places=2,max_digits=10,default=0.00)
	def __unicode__(self):

		return "cart id :%s"%(self.id )

class UserProfile(User):
	phone=models.CharField(max_length=225)
class abc(models.Model):
	phone=models.CharField(max_length=225)
class emp(models.Model):
	name=models.CharField(max_length=225)
	sal=models.DecimalField(decimal_places=2,max_digits=10)
	def __str__(self):
		return self.name,self.sal