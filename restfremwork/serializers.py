from rest_framework import serializers
from Apl.models import Customer,product,emp
class ExSerializer(serializers.ModelSerializer):
	class Meta:
		model=product
		fields=["Customer","des"]
class ExSerializerGet(serializers.ModelSerializer):
	class Meta:
		model=product
		fields=["Customer","des"]
class EmpSerializes(serializers.ModelSerializer):
	class Meta:
		model=emp
		fields=["name","addr"]
