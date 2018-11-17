# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from models import  todolist
from forms import createfrom
import csv  
from django.http import HttpResponse  

# Create your views here.
def todo_list(request):
	single_Category = request.GET.get("title")
	if single_Category:
		todo_list = todolist.objects.filter(Title=single_Category)
	else:

		todo_list=todolist.objects.all()
	return render(request,"app/todolist.html",{"todo_list":todo_list})
def edit(request,pk):
	todo_list=todolist.objects.get(pk=pk)
	return render(request,"app/todolist.html",{"todo_list":todo_list})
def Home(request):

	return render(request,"app/home.html")
def getfile(request):  
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="file.csv"'  
    todolists = todolist.objects.all()  
    writer = csv.writer(response)  
    for i in todolists:  
        writer.writerow([i.Title,i.Description,i.datetime,i.Status])  
    return response  


