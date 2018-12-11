# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from  rest_framework.response import Response
import json
from models import Customer,product,emp
from serializers import ExSerializer,ExSerializerGet,EmpSerializes
from rest_framework import status

# Create your views here.
class customerViwe(APIView):
	def put(self,request):
		return Response("helll word")
	def post(self,request):
		cus=Customer(**request.data)
		cus.save()
		return Response(" cusert save")
	def get(self,request):
		cust=[ i.name for i in Customer.objects.all()]
		return Response(cust)
class productViwe(APIView):
	def post(self,request):
		try:		
			poduct = ExpSerializer(data=request.data)
			if poduct.is_valid():
				poduct.save()
				return Response("poduct created successfully")
			else:
				return Response(poduct._errors,
					status=status.HTTP_400_BAD_REQUEST)
		except Exception as err:
			return Response(err.message,
				status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	def get(self,request):
		data=product.objects.all()
		pd=ExSerializerGet(data,many=True)
		return Response(pd.data)
class empView(APIView):
	def put(self,request):
		return Response("wellcome to emp")
	def post(self,request):
		Emp=EmpSerializes(data=request.data)
		if Emp.is_valid():
			Emp.save()
			return Response("created successfully")
	def get(self,request):
		Emp=emp.objects.all()
		sr=EmpSerializes(Emp,many=True)
		return Response(sr.data)





