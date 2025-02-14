# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Profession(models.Model):
	description = models.CharField(max_length=50)
	def __str__(self):
		return self.description
class DataSheet(models.Model):
    description = models.CharField(max_length=50)
    historical_data = models.TextField()
    def __str__(self):
    	return self.description


class Customer(models.Model):
	name = models.CharField(max_length=50)
	address = models.CharField(max_length=50)
	professions = models.ManyToManyField(Profession)
	data_sheet = models.OneToOneField(DataSheet, on_delete=models.CASCADE, null=True, blank=True)
    # doc_num = models.CharField(max_length=12, unique=True, null=True, blank=True)

	def __str__(self):
		return self.name




class Document(models.Model):
    PP = 'PP'
    ID = 'ID'
    OT = 'OT'

    DOC_TYPES = (
        (PP, 'Passport'),
        (ID, 'Identity card'),
        (OT, 'Others')
    )

    dtype = models.CharField(choices=DOC_TYPES, max_length=2)
    doc_number = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.doc_number
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField( default='python', max_length=100)
    style = models.CharField( default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)