from django.shortcuts import render, render_to_response
from sealadvisor.models import Advise, Application
from sealadvisor.forms import AddAdvise1, AddAdvise2, AddAdvise3, AddAdvise4, AddAdvise5, AddAdvise6
from formtools.wizard.views import SessionWizardView


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

def sterntube_chosen(wizard):
	cleaned_data = wizard.get_cleaned_data_for_step('0') or {}

	if cleaned_data.get('application') == 'sterntube':
		return False
	else: 
		return True

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

	def done(self, form_list, **kwargs):

		data = {}

		for form in form_list:
			data.update(form.cleaned_data)
			

		



		return render_to_response('sealadvisor/done.html', {
			'data': data,
		})


