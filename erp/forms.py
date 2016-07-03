from django import forms
from erp.models import Seal, Company, Part


class addSealForm(forms.ModelForm):
	class Meta:
		model = Seal
		fields = ('seal_type','x_number', 'company', 'size')

class addCompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ('name',)


class addPartForm(forms.ModelForm):
	class Meta:
		model = Part
		fields = ('number','category','size','name','description','material')