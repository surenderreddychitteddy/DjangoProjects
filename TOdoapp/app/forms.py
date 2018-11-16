from django import forms
from models import todolist
class createfrom(forms.ModelForm):
	class Meta:
		model=todolist
		fields="__all__"