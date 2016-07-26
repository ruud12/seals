from django import forms
from sealadvisor2.models import sealApplication, supremeAdvise, AftSealOptions, environmentalOptions,FwdSealOptions, Certificate
from erp.models import Company



class supremeSalesTypeForm(forms.Form):
	CHOICES = (
		('new','Supreme new'),
		('retrofit', 'Supreme retrofit'),
		('spares', 'Supreme spare parts')
	)

	sales_type = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
	company = company = forms.ModelChoiceField(queryset=Company.objects.all(), label='Customer')


	def clean_sales_type(self):

		sales_type = self.cleaned_data['sales_type']

		if sales_type == 'spares':
			raise forms.ValidationError('No spare parts wizard yet')

		return sales_type

	class Meta:
		fields = ('sales_type', )


class supremeWizard(forms.ModelForm):
	# is the code below required?
	# def __init__(self, *args, **kwargs):
	# 	self._aft_seal = kwargs.pop('aft_seal', None)
	# 	self._fwd_seal = kwargs.pop('fwd_seal', None)
	# 	super(supremeWizard, self).__init__(*args, **kwargs)


	error_css_class = 'error'


	def clean_aftSize(self):
		aftSize = self.cleaned_data['aftSize']
		aft_seal = self.cleaned_data.get('aft_seal')

		if aft_seal:
			if aftSize is not None:
				if aftSize > 900 or aftSize < 90:
					raise forms.ValidationError("Size must be between 90 and 900")
			else:
				raise forms.ValidationError('Size is required')
		
		return aftSize

	def clean_fwdSize(self):
		fwdSize = self.cleaned_data['fwdSize']
		fwd_seal = self.cleaned_data.get('fwd_seal')

		if fwd_seal:
			if fwdSize is not None:
				if fwdSize > 900 or fwdSize < 90:
					raise forms.ValidationError("Size must be between 90 and 900")
			else:
				raise forms.ValidationError('Size is required')
		
		return fwdSize


	def clean_aft_build_in_length(self):
		aft_build_in_length = self.cleaned_data['aft_build_in_length']

		aft_seal = self.cleaned_data.get('aft_seal')

		if aft_seal:
			if aft_build_in_length is not None:
				if aft_build_in_length < 10 or aft_build_in_length > 1000:
					raise forms.ValidationError('Built in length must be between 10 and 1000 mm')

		return aft_build_in_length







	def clean_rpm(self):
		rpm = self.cleaned_data['rpm']

		if ( rpm > 500 or rpm < 80 ):
			raise forms.ValidationError("RPM must be between 80 and 500")
		return rpm

	CHOICES = (
		('shaft', 'Shaft centered'),
		('hub', 'Hub centered'),
	)

	linerCentering = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

	class Meta:
		model = supremeAdvise
		fields = ('application','cpp_fpp','number_of_shafts', 'vgp', 'aft_seal','linerCentering', 'aftSize','aft_build_in_length','fwd_seal','fwdSize','rpm', 'draught_shaft','typeApproval','classCertificate')


class supremeAftForm(forms.ModelForm):

	CHOICES = (
		('shaft', 'Shaft centered'),
		('hub', 'Hub centered'),
	)

	linerCentering = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


	class Meta:
		model = AftSealOptions
		fields = ( 'linerCentering','seaguard', 'air', 'dirtBarrier','oring', 'anode', 'hml', 'distanceRing','wireWinders','netCutters','hastelloy')


class supremeFwdForm(forms.ModelForm):
	class Meta:
		model = FwdSealOptions
		fields = ('ocr', 'fkm')


class supremeEnvironmentForm(forms.ModelForm):
	OIL_CHOICES = (
		('mineral', 'Mineral oil'),
		('eal', 'EAL oil (bio degradable oil)'),
	)

	oil = forms.ChoiceField(widget=forms.RadioSelect, choices=OIL_CHOICES)

	class Meta:
		model = environmentalOptions
		fields = ('oil','oilType','vgp','air')