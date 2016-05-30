from django import forms
from seals.models import Action
from django.forms.extras.widgets import SelectDateWidget

class AddAction(forms.ModelForm):

	class Meta:
		model = Action

		remarks = forms.CharField(widget=forms.Textarea)
		execute_date = forms.DateField(
			widget=SelectDateWidget(
				empty_label=(
					"Choose Year", "Choose Month", "Choose Day"
				),
			),
		)
		fields = ('name', 'execute_date', 'remarks')