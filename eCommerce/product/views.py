 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from models import Product
from django.contrib .auth.models import User
from django.contrib.auth import authenticate
from models import UserProfile,Cart
from form import CustModelForm

# Create your views here.
def home(request):
	return render(request,'product/base.html')
def list_product(request):
	# lp=Product.objects.all()
	single_Category = request.GET.get("name")
	if single_Category:
		lp = Product.objects.filter(title=single_Category)
	else:
		lp=Product.objects.all()
	return render(request,'product/list_product.html',{"lp":lp})
def productprofile(request,pk):
	try:
		object=Product.objects.get(pk=pk)

	except Exception as e:
		raise e
	return render(request,'product/productprofile.html',{"object":object})
def SignUP(request):
	msg=" "
	if request.method=="POST":
		user=UserProfile.objects.create_user(username=request.POST.get("username"),
			password=request.POST.get("password"),phone=request.POST.get("phone"),email=request.POST.get('email'))
		user.save()
		msg="create user "
		
	return render(request,'product/SignUP.html',{"msg":msg})
def createproduct(request):
	if request.method=="POST":
		form=CustModelForm(request.POST,request.FILES)

		if form.is_valid():
			data=form.cleaned_data
			p=Product(**data)
			p.save()
	form=CustModelForm()

	return render(request,'product/createproduct.html',{"form":form})

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
	# def instructor(request):
# 	#import pdb; pdb.set_trace()
# 	single_instructor = request.GET.get("name")
# 	if single_instructor:
# 		data = Instructor.objects.filter(name=single_instructor)
# 	else:
# 		data = Instructor.objects.all()
# 	return render(request,"app1/list_instructor.html",{"data":data})



def controlpage(request):

	return render(request,'product/controlpage.html')
def addcart(request,pk):
	cart=Cart.objects.all()[0]
	try:
		pdt=Product.objects.get(pk=pk)
	except Exception as e:
		raise e
	finally:
		pass
	if not pdt in cart.product.all():#many to many filed
		cart.product.add(pdt)
	else:
		cart.product.remove(pdt)
	new_totl=0.00
	for i in cart.product.all():
		new_totl+=float(i.price)
	cart.total=new_totl
	cart.save()


	return redirect(viwecart)


def viwecart(request):

	cart=Cart.objects.all()[0]
	return render(request,'product/viwecart.html',{"cart":cart})



