from .models import  Customer,Profession,DataSheet,Document,Snippet

from rest_framework import serializers
class Customerserializer(serializers.ModelSerializer):
	class Meta:
		model=Customer
		fields="__all__"
class Professionserializer(serializers.ModelSerializer):
	class Meta:
		model=Profession
		fields="__all__"

class DataSheetserializer(serializers.ModelSerializer):
	class Meta:
		model=DataSheet
		fields="__all__"
class Documentserializer(serializers.ModelSerializer):
	class Meta:
		model=Document
		fields="__all__"
class Snippetserializer(serializers.ModelSerializer):
	class Meta:
		model=Snippet
		fields="__all__"