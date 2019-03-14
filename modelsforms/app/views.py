# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from forms import StudentModelForm
from models import Student,Userprofile
from django.contrib.auth.models import User

from django.contrib.auth import authenticate

# Create youStudentModelr views here.
def create(request):
	if request.method=="POST":
		cust=StudentModelForm(request.POST)

		if cust.is_valid():
			data=cust.cleaned_data
			t=Student(**data)
			t.save()
			return redirect('/profile/'+str(t.id)+'/')


	form =StudentModelForm()
	return render(request,"create.html",{"form":form})
def profile(request,id=id):
	st=Student.objects.get(id=id)
	return render(request,"profile.html",{"st":st})

def Registion(request):
	msg=""
	if request.method=="POST":
		user=Userprofile.objects.create_user(username=request.POST.get("username"),
			                            password=request.POST.get("password"),
			                            email=request.POST.get("email"),
			                           phone=request.POST.get("phone"),
			                           add=request.POST.get("add") )
		msg="create Registion success"
		return redirect("/login/")




	return render(request,'Registion.html',{"msg":msg})
def update(request,id=None):
	item=get_object_or_404(Student,id=id)



	cust=StudentModelForm(request.POST or None,instance=item)

	if cust.is_valid():

		data=cust.cleaned_data
		t=Student(**data)
		t.save()
		return redirect('/profile/'+str(t.id)+'/')


	form =StudentModelForm()
	return render(request,"create.html",{"form":form})





def login(request):
	msg=""
	if request.method=="POST":
		user=authenticate(username=request.POST.get("username"),
			          password=request.POST.get("password"))
		msg="login success"
		if user:
			return redirect("/create/")
	return render(request,'login.html',{"msg":msg})

	