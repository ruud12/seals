from django import forms
from isah.models import SealSize, SealType, Seal, SealCompany, SealVessel, LS, ContactPerson, ServiceReport

class SealForm(forms.ModelForm):

	size = forms.ModelChoiceField(SealSize.objects.order_by('size'), required=True)

	class Meta:
		model = Seal
		fields = ('company', 'vessel', 'serial_number','seal_type','size')


class SealSizeForm(forms.ModelForm):

	def clean_size(self):
		size = self.cleaned_data['size']

		if self.instance.id:
			# if editing this form an instance id exist, so exlude the current instance:
			if SealSize.objects.filter(size = size).exclude(pk=self.instance.id).count() > 0: # check if other objects with the same value exist
				raise forms.ValidationError('Size does already exist, try a different size')

		else:
			# new instance, so no id yet:
			if SealSize.objects.filter(size = size).count() > 0:
				raise forms.ValidationError('Size does already exist, try a different size')

		return size


	class Meta:
		model = SealSize
		fields = ('size',)



class SealTypeForm(forms.ModelForm):

	def clean_name(self):
		name = self.cleaned_data['name']

		if self.instance.id:
			# if editing this form an instance id exist, so exlude the current instance:
			if SealType.objects.filter(name = name).exclude(pk=self.instance.id).count() > 0:
				raise forms.ValidationError('Name does already exist, try a different name')
		else:
			# new instance, so no id yet:
			if SealType.objects.filter(name = name).count() > 0:
				raise forms.ValidationError('Name does already exist, try a different name')

		return name

	class Meta:
		model = SealType
		fields = ('name','description')




class SealCompanyForm(forms.ModelForm):

	class Meta:
		model = SealCompany
		fields = ('name', 'street_and_number', 'postal_code','city', 'province' )



class SealVesselForm(forms.ModelForm):

	class Meta:
		model = SealVessel
		fields = ('name','company','imo_number')


class LSForm(forms.ModelForm):

	class Meta:
		model = LS
		fields = ('LS_number','description','company', 'seals')


class ContactPersonForm(forms.ModelForm):

	class Meta:
		model = ContactPerson
		fields = ('company', 'first_name', 'last_name', 'email', 'position')


class ServiceReportForm(forms.ModelForm):

	remarks = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = ServiceReport
		fields = ('ls', 'date_from', 'date_to', 'superintendant', 'location', 'remarks')