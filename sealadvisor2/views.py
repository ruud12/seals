from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from sealadvisor2 import forms
from sealadvisor2.models import supremeAdvise, supremeFwdShaftInformation, supremeAftShaftInformation, environmentalInformation

# Create your views here.



def whichAirType(draught):
	return 'ventus' if draught > 4 else 'athmos'



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


	return render(request, 'sealadvisor2/add_supreme.html', {'form':form, 'title': "Add supreme advise"})



# def supreme(request):

# 	if request.method == "POST":
# 		form = forms.supremeWizard(request.POST)
# 		if form.is_valid():
# 			newAdvise = form.save()
# 			return redirect('sealadvisor2:index')
# 	else:
# 		form = forms.supremeWizard()


# 	return render(request, 'sealadvisor2/supreme.html', {'form':form})

def supremeDetail(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	return render(request,'sealadvisor2/supreme.html', {'advise':supreme})

def supremeEdit(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	company_id = supreme.company.pk if supreme.company else ''

	if request.method == "POST":
		form = forms.supremeWizard(request.POST, instance=supreme)

		if form.is_valid():
			updatedAdvise = form.save(commit=False)

			if updatedAdvise.application.key == 'sterntube':
				if not updatedAdvise.fwd_seal:
					updatedAdvise.fwd_shaft_information = None
				if not updatedAdvise.aft_seal:
					updatedAdvise.aft_shaft_information = None
			else:
				updatedAdvise.aft_seal = True
				updatedAdvise.fwd_seal = False
				updatedAdvise.fwd_shaft_information = None

			updatedAdvise.save()

			if updatedAdvise.environmental:
				updatedAdvise.environmental.zero_leakage_type = whichAirType(updatedAdvise.draught_shaft)
				updatedAdvise.environmental.save()



			return redirect('sealadvisor2:supremeDetail', supreme_id=supreme.id)
	else:
		form = forms.supremeWizard(initial={'company': company_id, 'application': supreme.application, 'cpp_fpp':supreme.cpp_fpp,'aft_seal':supreme.aft_seal,'fwd_seal':supreme.fwd_seal,'rpm':supreme.rpm,'draught_shaft':supreme.draught_shaft})

	return render(request,'sealadvisor2/add_supreme.html', { 'form':form, 'title':"Edit supreme advise"})


def supremeFwd(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	if request.method == "POST":
		form = forms.supremeFwdForm(request.POST)

		if form.is_valid():
			fwdInformation = form.save()
			supreme.fwd_shaft_information = fwdInformation
			supreme.save()

			return redirect('sealadvisor2:supremeDetail', supreme_id=supreme.id)
	else:
		form = forms.supremeFwdForm()

	return render(request,'sealadvisor2/seal_information.html', { 'form':form, 'supreme_id': supreme.id, 'title':"Forward shaft information"})



def supremeFwdEdit(request, supreme_id, fwd_id):
	fwd = get_object_or_404(supremeFwdShaftInformation, pk=fwd_id)

	if request.method == "POST":
		form = forms.supremeFwdForm(request.POST, instance=fwd)

		if form.is_valid():
			form.save()

			return redirect('sealadvisor2:supremeDetail', supreme_id=supreme_id)

	else:
		form = forms.supremeFwdForm(initial={"fwd_shaft_size": fwd.fwd_shaft_size,"fwd_pcd_liner": fwd.fwd_pcd_liner,"fwd_pcd_flange":fwd.fwd_pcd_flange,"fwd_centering_edge":fwd.fwd_centering_edge})

	return render(request,'sealadvisor2/seal_information.html', { 'form':form, 'supreme_id':supreme_id, 'title':"Forward shaft information" })



def supremeAft(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	if request.method == "POST":
		form = forms.supremeAftForm(request.POST)

		if form.is_valid():
			aftInformation = form.save()
			supreme.aft_shaft_information = aftInformation
			supreme.save()

			return redirect('sealadvisor2:supremeDetail', supreme_id=supreme.id)
	else:
		form = forms.supremeAftForm()

	return render(request,'sealadvisor2/seal_information.html', { 'form':form, 'supreme_id': supreme.id, 'title':"Aft shaft information"})



def supremeAftEdit(request, supreme_id, aft_id):
	aft = get_object_or_404(supremeAftShaftInformation, pk=aft_id)

	if request.method == "POST":
		form = forms.supremeAftForm(request.POST, instance=aft)

		if form.is_valid():
			form.save()

			return redirect('sealadvisor2:supremeDetail', supreme_id=supreme_id)

	else:
		form = forms.supremeAftForm(initial={"aft_shaft_size": aft.aft_shaft_size,"aft_pcd_liner": aft.aft_pcd_liner,"aft_pcd_flange":aft.aft_pcd_flange,"aft_centering_edge":aft.aft_centering_edge})

	return render(request,'sealadvisor2/seal_information.html', { 'form':form, 'supreme_id':supreme_id, 'title':"Aft shaft information" })



def environmental(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	if request.method == "POST":
		form = forms.supremeEnvironmentalForm(request.POST)

		if form.is_valid():
			environmental = form.save(commit=False)

			environmental.zero_leakage_type = whichAirType(supreme.draught_shaft)
			environmental.save()

			supreme.environmental = environmental
			supreme.save()

			return redirect('sealadvisor2:supremeDetail', supreme_id=supreme.id)
	else:
		form = forms.supremeEnvironmentalForm()

	return render(request,'sealadvisor2/seal_information.html', { 'form':form, 'supreme_id': supreme.id, 'title':"Environmental shaft information"})



def environmentalEdit(request, supreme_id, environmental_id):
	environmental = get_object_or_404(environmentalInformation, pk=environmental_id)
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	if request.method == "POST":
		form = forms.supremeEnvironmentalForm(request.POST, instance=environmental)

		if form.is_valid():
			environmental = form.save()

			return redirect('sealadvisor2:supremeDetail', supreme_id=supreme_id)

	else:
		form = forms.supremeEnvironmentalForm(initial={'eal':environmental.eal, 'vgp':environmental.vgp,'zero_leakage':environmental.zero_leakage })

	return render(request,'sealadvisor2/seal_information.html', { 'form':form, 'supreme_id':supreme_id, 'title':"Environmental information" })

