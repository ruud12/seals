from django import forms
from erp.models import Seal, Company


class addSealForm(forms.ModelForm):
	class Meta:
		model = Seal
		fields = ('seal_type','x_number', 'company', 'size')

class addCompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ('name',)