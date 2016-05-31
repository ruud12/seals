from django import forms
from sealadvisor.models import Advise, Application


class AddAdvise1(forms.ModelForm):
	error_css_class = 'error'

	class Meta:
		model = Advise
		fields = ('application', 'shaft_size', 'rpm', 'draught_shaft')

		
class AddAdvise2(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('forwardseal', 'aftseal')		


class AddAdvise3(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('eal','liner_centering','oring')



