from django.shortcuts import render, render_to_response
from sealadvisor.models import Advise, Application
from sealadvisor.forms import Advise0, Advise1, Advise2, Advise3, Advise4,Advise5, Advise6
from seals.models import Company
from formtools.wizard.views import SessionWizardView
import sys

# Create your views here.

# def index(request):

# 	if request.method == "POST":
# 		form = AddAdvise1(request.POST)
# 		# if form.is_valid():
# 			# new_action = form.save(commit=False)
# 			# new_action.relatedtoseal = get_object_or_404(Seal, pk=seal_id)
# 			# new_action.relatedtoreport = get_object_or_404(Report, pk=report_id)
# 			# new_action.save()
# 			# return redirect('seals:detail', primary_key=seal_id)

# 	else:
# 		form = AddAdvise1()

# 	return render(request, 'sealadvisor/index.html', { 'form': form })


def index(request):
	return render(request, 'sealadvisor/index.html')


def sterntube_chosen(wizard):
	cleaned_data = wizard.get_cleaned_data_for_step('0') or {}

	try:
		return cleaned_data.get('application', 'None').key =='sterntube'
	except Exception:
		return False



def aft(wizard):
	step0 = wizard.get_cleaned_data_for_step('0') or {}
	step1 = wizard.get_cleaned_data_for_step('1') or {}

	try:
		return step0.get('application', 'None').key != 'sterntube' or (step0.get('application', 'None').key == 'sterntube' and step1.get('aftseal', 'None') == True)
	except Exception:
		return False


def forward(wizard):
	step0 = wizard.get_cleaned_data_for_step('0') or {}
	step1 = wizard.get_cleaned_data_for_step('1') or {}

	try:
		return (step0.get('application', 'None').key == 'sterntube' and step1.get('forwardseal', 'None') == True)
	except Exception:
		return False



def ventus(wizard):
	cleaned_data = wizard.get_cleaned_data_for_step('0') or {}

	if cleaned_data:
		if cleaned_data.get('draught_shaft') > 4:
			return True
		else:
			return False
	else:
		return False

def athmos(wizard):
	cleaned_data = wizard.get_cleaned_data_for_step('0') or {}
	if cleaned_data:
		if cleaned_data.get('draught_shaft') > 4:
			return False
		else:
			return True
	else:
		return False



class ContactWizard(SessionWizardView):

	template_name = "sealadvisor/sealadvisor_template.html"

	def parse_params(self, request, *args, **kwargs):
		current_step = self.determine_step(request, *args, **kwargs)

		if request.method == 'POST' and current_step == 1:
			form = self.get_form(current_step, request.POST)
			if form.is_valid():
			# 	self.initial[(current_step + 2)] = {
			# 		'forwardseal' : True,
			# 		# 'name': form.cleaned_data['name'],
			# 		# 'address': form.cleaned_data['address'],
			# 		# 'city': form.cleaned_data['city'],
			# 	}


				del self.fields[(current_step+1)]['application']

	def done(self, form_list, **kwargs):

		data = {}

		for form in form_list:
			data.update(form.cleaned_data)
			

		return render_to_response('sealadvisor/done.html', {
			'data': data,
		})


