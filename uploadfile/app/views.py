# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from forms import DocumentForm
from models import Document

# Create your views here.
def uploadfile(request):
	if request.method=="POST":
		doc=DocumentForm(request.POST,request.FILES)
		if doc.is_valid():
			doc.save()
			return redirect("/home/")
	form=DocumentForm()
	return render(request,"uploadfile.html",{"form":form})
def home(request):
	doc=Document.objects.all()
	return render(request,'home.html',{"doc":doc})


