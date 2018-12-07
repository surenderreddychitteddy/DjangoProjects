# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import Customer,Profession,Document,DataSheet,Snippet
admin.site.register(Customer)
admin.site.register(Document)
admin.site.register(Profession)
admin.site.register(DataSheet)
admin.site.register(Snippet)