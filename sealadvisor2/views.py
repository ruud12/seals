from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from sealadvisor2 import forms
from sealadvisor2.models import supremeAdvise

# Create your views here.

def index(request):
	supremeAdvises = supremeAdvise.objects.all()
	return render(request, 'sealadvisor2/index.html', {'supreme':supremeAdvises})


def supreme(request):

	if request.method == "POST":
		form = forms.supremeWizard(request.POST)
		if form.is_valid():
			newAdvise = form.save()
			return redirect('sealadvisor2:index')
	else:
		form = forms.supremeWizard()


	return render(request, 'sealadvisor2/supreme.html', {'form':form})


def supremeDetail(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	company_id = supreme.company.pk if supreme.company else ''

	if request.method == "POST":
		form = forms.supremeWizard(request.POST, instance=supreme)

		if form.is_valid():
			updatedAdvise = form.save()
			return redirect('sealadvisor2:supremeDetail', supreme_id=supreme.id)
	else:
		form = forms.supremeWizard(initial={'company': company_id, 'application': supreme.application, 'cpp_fpp':supreme.cpp_fpp,'aft_seal':supreme.aft_seal,'fwd_seal':supreme.fwd_seal,'rpm':supreme.rpm,'draught_shaft':supreme.draught_shaft})

	return render(request,'sealadvisor2/supreme.html', { 'form':form, 'advise':supreme})


def supremeFwd(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	if request.method == "POST":
		form = forms.supremeFwdForm(request.POST)

		if form.is_valid():
			fwdInformation = form.save()
			supreme.fwd_seal_information = fwdInformation
			supreme.save()

			return redirect('sealadvisor2:supremeDetail', supreme_id=supreme.id)
	else:
		fwdInformation = get_object_or_404(supremeFwdShaftInformation, pk=supreme.fwd_seal_information.id)
		form = forms.supremeFwdForm()

	return render(request,'sealadvisor2/seal_information.html', { 'form':form, 'advise': supreme})



