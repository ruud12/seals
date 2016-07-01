from django import forms
from sealadvisor2.models import sealApplication, supremeAdvise, AftSealOptions, environmentalOptions,FwdSealOptions
from seals.models import Company






class supremeWizard(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self._aft_seal = kwargs.pop('aft_seal', None)
		self._fwd_seal = kwargs.pop('fwd_seal', None)
		super(supremeWizard, self).__init__(*args, **kwargs)


	error_css_class = 'error'


	def clean_aftSize(self):

		aftSize = self.cleaned_data['aftSize']
		if aftSize is not None:
			if aftSize > 900 or aftSize < 110:
				raise forms.ValidationError("Size must be between 110 and 900")

		return aftSize

	def clean_fwdSize(self):

		fwdSize = self.cleaned_data['fwdSize']
		if fwdSize is not None:
			if fwdSize > 900 or fwdSize < 110:
				raise forms.ValidationError("Size must be between 110 and 900")

		return fwdSize




	def clean_rpm(self):
		rpm = self.cleaned_data['rpm']

		if ( rpm > 500 or rpm < 80 ):
			raise forms.ValidationError("RPM must be between 80 and 500")
		return rpm

	class Meta:
		model = supremeAdvise
		fields = ('application','cpp_fpp','pressure_oring', 'aft_seal','aftSize','fwd_seal','fwdSize','rpm', 'draught_shaft','typeApproval')


class supremeAftForm(forms.ModelForm):
	class Meta:
		model = AftSealOptions
		fields = ( 'linerCentering','seaguard', 'dirtBarrier','oring', 'hml', 'distanceRing','wireWinders','netCutters','hastelloy','air')


class supremeFwdForm(forms.ModelForm):
	class Meta:
		model = FwdSealOptions
		fields = ('ocr', 'fkm')


class supremeEnvironmentForm(forms.ModelForm):
	class Meta:
		model = environmentalOptions
		fields = ('oil','oilType','vgp','air')