# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Customer,Profession,DataSheet,Document,Snippet
from django.shortcuts import render
from seializers import Customerserializer,Professionserializer,DataSheetserializer,Documentserializer,Snippetserializer
from rest_framework import viewsets
# from rest_framework.filters import DjangoFilterBackend

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class CusromerViewSet(viewsets.ModelViewSet):
	queryset=Customer.objects.all()
	serializer_class=Customerserializer
    # filter_fields = ('name' )



class ProfessionViewSet(viewsets.ModelViewSet):
	queryset=Profession.objects.all()
	serializer_class=Professionserializer
class DataSheetViewSet(viewsets.ModelViewSet):
	queryset=DataSheet.objects.all()
	serializer_class=DataSheetserializer
class DocumentViewSet(viewsets.ModelViewSet):
	queryset=Document.objects.all()
	serializer_class=Documentserializer
class SnippetList(APIView):

	def get(self,request):
		snippets=Snippet.objects.all()
		serializer = Snippetserializer(snippets, many=True)

		return Response(serializer.data)
	def post(self,request):
		serializer = Snippetserializer(request.data)
		if serializer.is_valid():
			serializer.save()
			return Response("created new record")
		else:
			return Response("not created")




class SnippetDetail(APIView):
	def get_object(self,pk):
		return Snippet.objects.get(pk=pk)
	def get(self,request,pk):
		# snippets=Snippet.objects.get(pk=pk)# overriden by get_object
		snippets=self.get_object(pk)
		serializer = Snippetserializer(snippets)

		return Response(serializer.data)
	def put(self, request, pk):
		snippet = self.get_object(pk)
		serializer = Snippetserializer(snippet, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response("not created")

	def delete(self, request, pk):
		snippet = self.get_object(pk)
		snippet.delete()
		return Response("delete suceesfully")
