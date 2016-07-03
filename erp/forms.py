from django import forms
from erp.models import Seal, Company, Part, sealComponent


class addSealForm(forms.ModelForm):
	class Meta:
		model = Seal
		fields = ('seal_type','x_number', 'company', 'size','vessel')

class addCompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ('name',)


class addPartForm(forms.ModelForm):
	class Meta:
		model = Part
		fields = ('number','category','size','name','description','material')


class addComponentToSealForm(forms.ModelForm):

	def __init__(self,*args,**kwargs):
		self.size = kwargs.pop('size')
		super(addComponentToSealForm, self).__init__(*args,**kwargs)
		self.fields['part'].queryset = Part.objects.filter(size=self.size)


	class Meta:
		model = sealComponent
		fields = ('number','part','status')