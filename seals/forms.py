from django import forms
from seals.models import Action, Report, contactPerson,Seal, Vessel, Company, contactPerson
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
	def __init__(self, *args, **kwargs):
		choices = kwargs.pop('choices')
		super(AddReport, self).__init__(*args, **kwargs)
		self.fields['mechanics'] = forms.MultipleChoiceField(
			choices = choices
		)

	# created = forms.DateTimeField(widget=forms.SplitDateTimeWidget(), initial=timezone.now())
	remarks = forms.CharField(widget=forms.Textarea)



	class Meta:
		model = Report

		fields = ('title', 'relatedtoseal', 'remarks', 'created')

		exclude = ('relatedtoseal',)



class AddSeal(forms.ModelForm):
	class Meta:
		model=Seal
		fields = ('serial_number','size','installedinvessel')


class AddContact(forms.ModelForm):
	class Meta:
		model = contactPerson
		fields = ('first_name','last_name','position','phone_number')

class EditContact(forms.ModelForm):
	class Meta:
		model = contactPerson
		fields = ('first_name','last_name','position','phone_number','company')
	
class DeleteSeal(forms.ModelForm):

	confirmation = forms.BooleanField(initial=False,label='I really want to delete this seal.')

	class Meta:
		model = Seal
		fields = ('confirmation',)

class EditSeal(forms.ModelForm):
	class Meta:
		model = Seal
		fields = ('serial_number','size','installedinvessel', 'status')

class EditVessel(forms.ModelForm):
	class Meta:
		model = Vessel
		fields = ('name','imo_number','company','contact')

class EditCompany(forms.ModelForm):
	class Meta:
		model = Company
		fields = ('name','street','streetNumber','city','country')