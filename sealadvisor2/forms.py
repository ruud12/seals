from django import forms
from sealadvisor2.models import sealApplication, supremeAdvise
from seals.models import Company






class supremeWizard(forms.ModelForm):
	error_css_class = 'error'

	class Meta:
		model = supremeAdvise
		fields = ('application','cpp_fpp','aft_seal','aftSize','fwd_seal','fwdSize','rpm', 'draught_shaft','typeApproval')

