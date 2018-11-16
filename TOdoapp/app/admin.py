# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from models import todolist
class  TodoListAdim(admin.ModelAdmin):
	search_fields=['Title','Status']
	list_display=['Title','Status','datetime','Status','Createdat','Modifiedat']
	class Meta:
		model=todolist
admin.site.register(todolist,TodoListAdim)
