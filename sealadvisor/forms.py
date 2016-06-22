from django import forms
from sealadvisor.models import Advise, Application
from seals.models import Company






class Advise0(forms.ModelForm):
	error_css_class = 'error'

	class Meta:
		model = Advise
		fields = ('application', 'cpp_fpp')


class Advise1(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('shaft_size', 'shaft_size_forward', 'rpm', 'draught_shaft')

	def __init__(self, *args, **kwargs):
		super(Advise1, self).__init__(*args, **kwargs)

		

	
class Advise2(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('forwardseal', 'aftseal')		


class Advise3(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('anode', 'eal','liner_centering','oring')


class Advise4(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('ventus',)

class Advise5(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('athmos',)

class Advise6(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('wirewinder', 'netcutters')