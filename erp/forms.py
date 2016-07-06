from django import forms
from erp.models import Seal, Company, Part, sealComponent, serviceReport, confirmComponentChange, Vessel, Mechanic, partMaterial, partCategory, contactPerson



class selectCompany(forms.Form):
	company = forms.ModelChoiceField(queryset=Company.objects.all())



class addSealForm(forms.ModelForm):
	class Meta:
		model = Seal
		fields = ('seal_type','x_number', 'company', 'size','vessel')

class addCompanyForm(forms.ModelForm):
	class Meta:
		model = Company
		fields = ('name',)

class addContactPersonForm(forms.ModelForm):
	class Meta:
		model = contactPerson
		fields = ('first_name','last_name','company','position')

class addMaterialForm(forms.ModelForm):
	class Meta:
		model = partMaterial
		fields = ('name',)

class addCategoryForm(forms.ModelForm):
	class Meta:
		model = partCategory
		fields = ('name',)

class addMechanicForm(forms.ModelForm):
	class Meta:
		model = Mechanic
		fields = ('first_name','last_name')

class addVesselForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		self.company_id = kwargs.pop('company_id')
		super(addVesselForm, self).__init__(*args,**kwargs)
		self.fields['contacts'].queryset = contactPerson.objects.filter(company=self.company_id)


	class Meta:
		model = Vessel
		fields = ('name','imo','company','contacts')


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


class addServiceReportForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		self.seal_id = kwargs.pop('seal_id')
		super(addServiceReportForm, self).__init__(*args,**kwargs)
		self.fields['parts_to_replace'].queryset = sealComponent.objects.filter(seal=self.seal_id)

	class Meta:
		model = serviceReport
		fields = ('name','date','mechanics','superintendant', 'parts_to_replace')



class confirmComponentChangeForm(forms.ModelForm):

	class Meta:
		model = confirmComponentChange
		fields = ('old_part', 'new_part', 'confirm')



