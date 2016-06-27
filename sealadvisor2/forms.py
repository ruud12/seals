from django import forms
from sealadvisor2.models import sealApplication, supremeAdvise, supremeAftShaftInformation, supremeFwdShaftInformation, environmentalInformation
from seals.models import Company






class supremeWizard(forms.ModelForm):
	error_css_class = 'error'

	class Meta:
		model = supremeAdvise
		fields = ('company', 'application','cpp_fpp','aft_seal','fwd_seal','rpm', 'draught_shaft','typeApproval')

class supremeFwdForm(forms.ModelForm):

	class Meta:
		model = supremeFwdShaftInformation
		fields = ('fwd_shaft_size','fwd_pcd_liner','fwd_pcd_flange','fwd_centering_edge')

class supremeAftForm(forms.ModelForm):

	class Meta:
		model = supremeAftShaftInformation
		fields = ('aft_shaft_size','aft_pcd_liner','aft_pcd_flange','aft_centering_edge')



class supremeEnvironmentalForm(forms.ModelForm):
	class Meta:
		model= environmentalInformation
		fields = ('eal','vgp','zero_leakage')