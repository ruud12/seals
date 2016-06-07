from django import forms
from sealadvisor.models import Advise, Application








class AddAdvise1(forms.ModelForm):
	error_css_class = 'error'
	# application = forms.ModelChoiceField(queryset=Application.objects.all(), widget=forms.RadioSelect)

	class Meta:
		model = Advise
		CHOICES = [(l.id, l.name) for l in Application.objects.all()]
		# application = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

		fields = ('application', 'shaft_size', 'rpm', 'draught_shaft')






		
class AddAdvise2(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('forwardseal', 'aftseal')		


class AddAdvise3(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('anode', 'eal','liner_centering','oring')


class AddAdvise4(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('ventus',)

class AddAdvise5(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('athmos',)

class AddAdvise6(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('wirewinder', 'netcutters')