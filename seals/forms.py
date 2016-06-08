from django import forms
from seals.models import Action, Report
from django.forms.extras.widgets import SelectDateWidget
from django.utils import timezone

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


class AddReport(forms.ModelForm):

	# created = forms.DateTimeField(widget=forms.SplitDateTimeWidget(), initial=timezone.now())
	# created = forms.DateTimeField(initial=timezone.now())
	remarks = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Report

		fields = ('title', 'relatedtoseal', 'remarks', 'created')

		exclude = ('relatedtoseal','created')