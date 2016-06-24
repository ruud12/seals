from django import forms
from sealadvisor.models import Advise, Application
from seals.models import Company






class Advise0(forms.ModelForm):
	error_css_class = 'error'

	class Meta:
		model = Advise
		fields = ('application', 'cpp_fpp','rpm','draught_shaft','liner_centering')


class Advise1(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('forwardseal', 'aftseal')		

class Advise2(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('shaft_size','aft_built_in_length','aft_pcd_liner', 'aft_liner_centering_edge', 'aft_pcd_flange', 'aft_pcd_centering')


class AftOptions(forms.ModelForm):
	class Meta:
		model = Advise
		fields = ('eal','wirewinder', 'netcutters', 'sandy', 'anode','hml_forward' )


class Advise3(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('shaft_size_forward','forward_pcd_flange', 'forward_pcd_centering')


class ForwardOptions(forms.ModelForm):
	class Meta:
		model = Advise
		fields = ('ocr','fkm_forward','hml_forward')


class Advise4(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('oring',)


class Advise5(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('ventus',)

class Advise6(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('athmos',)

class Advise7(forms.ModelForm):

	class Meta:
		model = Advise
		fields = ('wirewinder', 'netcutters')

class Other(forms.ModelForm):
	class Meta:
		model = Advise
		fields = ('type_approval','vgp')