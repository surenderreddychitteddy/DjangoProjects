from rest_framework import serializers
from models import school,student

class Schoolserializer(serializers.ModelSerializer):
	class Meta:
		model=school
		fields=["name","add"]
class studentSerializer(serializers.ModelSerializer):
	class Meta:
		model=student
		fields=["School","name"]