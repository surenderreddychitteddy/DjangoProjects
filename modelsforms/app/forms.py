# from django import forms
# from models import table
# class CustModelForm(forms.ModelForm):
# 	class Meata:
# 		model=table
# 		fields=["phone","email"]
# 		


from django import forms
from models import Student
# two kinds of forms: Normal forms, forms.Form and model forms, forms.ModelForm



class StudentModelForm(forms.ModelForm):
	class Meta:
		model=Student
		fields ="__all__"



