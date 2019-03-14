# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import Cart,Product,Cake,Gift,Catagery,Products,emp
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Cake)

admin.site.register(Gift)
admin.site.register(Catagery)

admin.site.register(Products)

admin.site.register(emp)
