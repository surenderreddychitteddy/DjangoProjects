 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from models import Product
from django.contrib .auth.models import User
from django.contrib.auth import authenticate
from models import UserProfile,Cart,Cake,Gift
from form import CustModelForm
from django.shortcuts import render, get_object_or_404

# Create your views here.


def home(request):
	return render(request,'product/base.html')
def SignUP(request):
	msg=" "
	if request.method=="POST":
		user=UserProfile.objects.create_user(username=request.POST.get("username"),
			password=request.POST.get("password"),phone=request.POST.get("phone"),email=request.POST.get('email'))
		user.save()
		msg="create user "
		
	return render(request,'product/SignUP.html',{"msg":msg})

def Login(request):
	msg=""
	request.session["user"] = None
	if request.method=="POST":
		user=authenticate(username=request.POST.get("username"),
			password=request.POST.get("password"))

		if user:
			# return redirect(list_product)
			user_profiles=UserProfile.objects.filter(user_ptr=user)
			if user_profiles:
				user_profile=user_profiles[0]
				request.session['user']={"username":user.username,"id":user_profile.id}
				return redirect(controlpage)
			else:
				msg="User profile not found for this user"
		else:
			msg="login failed"
	return render(request,'product/login.html',{"msg":msg})

def controlpage(request):

	return render(request,'product/controlpage.html')
def addcart(request,pk):

	cart=Cart.objects.all()[0]
	try:
		pdt=Cake.objects.get(pk=pk)
	except Exception as e:
		raise e
	finally:
		pass
	if not pdt in cart.cake.all():#many to many filed
		cart.cake.add(pdt)
	else:
		cart.cake.remove(pdt)
	new_totl=0.00
	for i in cart.cake.all():
		new_totl+=float(i.price)
	cart.total=new_totl
	cart.save()


	return redirect(viwecart)


def viwecart(request):

	cart=Cart.objects.all()[0]
	return render(request,'product/viwecart.html',{"cart":cart})



def cake(request):
	cake_list=Cake.objects.all()
	return render(request,'product/cake-list.html',{"cake_list":cake_list})


def gift(request):
	list_data=Gift.objects.all()
	return render(request,'product/gift-list.html',{"list_data":list_data})

def cakeprofile(request,pk):
	try:
		object=Cake.objects.get(pk=pk)

	except Exception as e:
		raise e
	return render(request,'product/cakeprofile.html',{"object":object})

def giftprofile(request,pk):
	try:
		object=Gift.objects.get(pk=pk)

	except Exception as e:
		raise e
	return render(request,'product/profile.html',{"object":object})

# 