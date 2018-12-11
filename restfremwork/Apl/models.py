# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your models here.
class Customer(models.Model):
	name=models.CharField(max_length=220)
	addr=models.CharField(max_length=220)
class product(models.Model):
	Customer=models.ForeignKey(Customer)
	des=models.CharField(max_length=250)
class emp(models.Model):
	name=models.CharField(max_length=220)
	addr=models.CharField(max_length=220)
class profile(models.Model):
	user=models.OneToOneField(User)
	name=models.CharField(max_length=220)
@receiver(post_save,sender=User)
def user_is_create(sender,instance,create,**kwargs):
	if create:
		profile.objects.create(user=instance.profile)
	else:
		instance.profile.save()


