# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from models import school,student
from serializers import Schoolserializer,studentSerializer
# Create your views here.
class studyhall(APIView):
	# def put(self,request):

	# 	return Response("hello pavan")
	# def post(self,request):
	# 	sc=school(**request.data)
	# 	sc.save()
	# 	return Response("created school")
	# def get(self,request):
	# 	s=[i.name  for i in school.objects.all()]
	# 	return Response(s)
	def post(self,request):
		sc=Schoolserializer(data=request.data)
		if sc.is_valid():
			sc.save()
			return Response("created")
		return Response(sc.errors,status=status.HTTP_400_BAD_REQUEST)
	def get(self,request):
		s=school.objects.all()
		sc=Schoolserializer(s,many=True)
		return Response(sc.data)
class studyhalldeatail(APIView):
	def put(self,request,pk):
		s=school.objects.get(pk=pk)
		sc=Schoolserializer(data=request.data)
		if sc.is_valid():
			sc.save()
			return Response(sc.data)
			
class expens(APIView):
	# def post(self,request):
	# 	try:
	# 		sc=school.objects.get(pk=request.data.get("School"))
	# 		request.data.update({"School":sc})
	# 		st=student(**request.data)
	# 		st.save()
	# 		return Response("created student ")
	# 	except Exception as err:
	# 		return Response(err.message,status=status.HTTP_400_BAD_REQUEST)
	def post(self,request):
		st=studentSerializer(data=request.data)
		if st.is_valid():
			st.save()
			return Response("created successfully")
		else:
			return response(st._errors,status=status.HTTP_400_BAD_REQUEST)
	def get(self,request):
		s=student.objects.all()
		st=studentSerializer(s,many=True)
		return Response(st.data)

















		



