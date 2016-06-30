from django import forms
from sealadvisor2.models import sealApplication, supremeAdvise, AftSealOptions, environmentalOptions
from seals.models import Company






class supremeWizard(forms.ModelForm):
	error_css_class = 'error'

	def clean_aftSize(self):
		aftSize = self.cleaned_data['aftSize']
		if aftSize > 900 or aftSize < 110:
			raise forms.ValidationError("Size must be between 110 and 900")
		
		return aftSize

	def clean_rpm(self):
		rpm = self.cleaned_data['rpm']

		if ( rpm > 500 or rpm < 80 ):
			raise forms.ValidationError("RPM must be between 80 and 500")
		return rpm

	class Meta:
		model = supremeAdvise
		fields = ('application','cpp_fpp','aft_seal','aftSize','fwd_seal','fwdSize','rpm', 'draught_shaft','typeApproval')


class supremeAftForm(forms.ModelForm):
	class Meta:
		model = AftSealOptions
		fields = ( 'linerCentering','seaguard', 'dirtBarrier','oring', 'hml', 'distanceRing','wireWinders','netCutters','hastelloy','air')




class supremeEnvironmentForm(forms.ModelForm):
	class Meta:
		model = environmentalOptions
		fields = ('oil','vgp','air')