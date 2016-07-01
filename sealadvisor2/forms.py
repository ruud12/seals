from django import forms
from sealadvisor2.models import sealApplication, supremeAdvise, AftSealOptions, environmentalOptions
from seals.models import Company






class supremeWizard(forms.ModelForm):
	error_css_class = 'error'

	class Meta:
		model = supremeAdvise
		fields = ('application','cpp_fpp','aft_seal','aftSize','fwd_seal','fwdSize','rpm', 'draught_shaft','typeApproval')


class supremeAftForm(forms.ModelForm):
	class Meta:
		model = AftSealOptions
		fields = ( 'linerCentering','seaguard', 'dirtBarrier','oring', 'hml', 'distanceRing','wireWinders','netCutters','hastelloy')




class supremeEnvironmentForm(forms.ModelForm):
	class Meta:
		model = environmentalOptions
		fields = ('oil','vgp','air')