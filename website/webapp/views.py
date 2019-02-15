# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from models import UserProfile

# Create your views here.
def home(request):
	return render(request,"base.html")
def Introduction(request):
	return render(request,'Introduction.html')
def Vision(request):
	return render(request,"Vision.html")
def ContactUs(request):
	return render(request,"ContactUs.html")
def EmplyoeeSignup(request):
	msg=" "
	if request.method=="POST":
		user=UserProfile.objects.create_user(email=request.POST.get('email'),
			             username=request.POST.get('username'),
			             password=request.POST.get('password'),
			             phonenumber=request.POST.get('phone'),
			             empid=request.POST.get('empid'),
			             name=request.POST.get('name'))
		msg="register created successfully! "
	return render(request,'EmplyoeeSignup.html',{"msg":msg})
def EmplyoeeLogin(request):
	msg=" "
	if request.method=="POST":
		user=authenticate(username=request.POST.get('username'),
			              password=request.POST.get('password'))
		msg=" login successfully"
		if user:
			return redirect("/addemploye/")
		else:
			return render(request,'EmplyoeeLogin.html',{"msg":"login failed"})
	return render(request,'EmplyoeeLogin.html')
def addemploye(request):
	user=UserProfile.objects.all()
	return render(request,'addemploye.html',{"user":user})
def UMS(request):
	return render(request,'ums.html')
