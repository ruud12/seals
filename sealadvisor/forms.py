from django import forms
from sealadvisor.models import Advise, Application


class AddAdvise1(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('application', 'shaft_size_aft', 'shaft_size_forward', 'rpm', 'draught_shaft')

		
class AddAdvise2(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('forwardseal', 'aftseal')		


class AddAdvise3(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('eal',)

