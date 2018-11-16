# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import Cart,Product
admin.site.register(Cart)
admin.site.register(Product)

