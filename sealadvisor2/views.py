from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponseRedirect
from sealadvisor2 import forms
from sealadvisor2.models import supremeAdvise, AftSealOptions, environmentalOptions
import bisect, decimal
from django.core.urlresolvers import reverse
# Create your views here.







def whichAirType(draught):
	return 'ventus' if draught > 4 else 'athmos'


def findCorrectSize(shaft_diameter):
	# check for the closest liner value taking into account a 1 cm liner thickness

	available_sizes = [110,125,155,175,200,225,260,330,355,440,600,720,800,900,1000]
	n = bisect.bisect_left(available_sizes,shaft_diameter+10)
	return available_sizes[n]





def index(request):
	advises = supremeAdvise.objects.all()

	return render(request, 'sealadvisor2/index.html', {'advises': advises})


def supreme(request):
	if request.method == "POST":
		form = forms.supremeWizard(request.POST)
		if form.is_valid():
			newAdvise = form.save()
			
			if ((newAdvise.application.key =='sterntube' or newAdvise.aft_seal) and not newAdvise.aft):
				return redirect('sealadvisor2:supremeAft',newAdvise.id)
			else:
				return redirect('sealadvisor2:supremeEnvironment', newAdvise.id)

	else:
		form = forms.supremeWizard()


	return render(request, 'sealadvisor2/add_supreme.html', {'form':form, 'title': "Add supreme advise", 'submit':'Next'})




def supremeEdit(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	if request.method == "POST":
		form = forms.supremeWizard(request.POST, instance=supreme)
		if form.is_valid():
			form.save()
			
			return redirect('sealadvisor2:supremeOverview',supreme_id)

	else:
		form = forms.supremeWizard(initial={'application': supreme.application.id, 'cpp_fpp': supreme.cpp_fpp, 'fwd_seal': supreme.fwd_seal, 'aft_seal': supreme.aft_seal, 'aftSize': supreme.aftSize, 'fwdSize': supreme.fwdSize, 'rpm': supreme.rpm, 'draught_shaft': supreme.draught_shaft, 'aft': supreme.aft.id, 'environment': supreme.environment.id, 'typeApproval':supreme.typeApproval.id })


	return render(request, 'sealadvisor2/add_supreme.html', {'form':form, 'title': "Edit Supreme advise", 'submit':'Save'})






def supremeAft(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	if request.method == "POST":
		form = forms.supremeAftForm(request.POST)
		if form.is_valid():
			aftOptions = form.save()
			supreme.aft = aftOptions
			supreme.save()

			return redirect('sealadvisor2:supremeEnvironment', supreme_id)

	else:

		form = forms.supremeAftForm()

	return render(request, 'sealadvisor2/seal_information.html', {'form':form, 'title': 'Aft seal options','submit':'Next'})



def supremeAftEdit(request, supreme_id, aft_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)
	aft = get_object_or_404(AftSealOptions, pk=aft_id)

	if request.method == "POST":
		form = forms.supremeAftForm(request.POST, instance=aft)
		if form.is_valid():
			aftOptions = form.save()

			return redirect('sealadvisor2:supremeOverview', supreme_id)

	else:
		form = forms.supremeAftForm(initial={'seaguard':aft.seaguard, 'oring': aft.oring, 'linerCentering':aft.linerCentering,'distanceRing':aft.distanceRing, 'dirtBarrier': aft.dirtBarrier,'wireWinders':aft.wireWinders,'netCutters': aft.netCutters, 'hastelloy': aft.hastelloy})
		print(aft.linerCentering)

	return render(request, 'sealadvisor2/seal_information.html', {'form':form, 'title': 'Edit aft seal options','submit':'Save'})







def supremeEnvironment(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)
	pv = (supreme.aftSize / 1000) * decimal.Decimal(3.14) * (supreme.rpm / 60) * (supreme.draught_shaft / 10)
	air_type= 'Ventus' if supreme.draught_shaft >= 5 else 'Athmos'

	if request.method == 'POST':
		form = forms.supremeEnvironmentForm(request.POST)
		if form.is_valid():
			environmentalOptions = form.save()
			supreme.environment = environmentalOptions
			supreme.save()

			return redirect('sealadvisor2:supremeOverview', supreme_id)

	else:
		form = forms.supremeEnvironmentForm()

	return render(request, 'sealadvisor2/seal_information.html', {'form':form, 'title': 'Environmental information','air_type':air_type,'pv':pv,'submit':'Next'})


def supremeEnvironmentEdit(request, supreme_id, env_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)
	env = get_object_or_404(environmentalOptions, pk=env_id)

	pv = (supreme.aftSize / 1000) * decimal.Decimal(3.14) * (supreme.rpm / 60) * (supreme.draught_shaft / 10)
	air_type= 'Ventus' if supreme.draught_shaft >= 5 else 'Athmos'

	if request.method == 'POST':
		form = forms.supremeEnvironmentForm(request.POST, instance = env)
		if form.is_valid():
			form.save()

			return redirect('sealadvisor2:supremeOverview', supreme_id)

	else:
		form = forms.supremeEnvironmentForm(initial = {'vgp':env.vgp, 'oil': env.oil, 'air': env.air})

	return render(request, 'sealadvisor2/seal_information.html', {'form':form, 'title': 'Environmental information','air_type':air_type,'pv':pv,'submit':'Save'})






def supremeOverview(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	pv = (supreme.aftSize / 1000) * decimal.Decimal(3.14) * (supreme.rpm / 60) * (supreme.draught_shaft / 10)
	air_type= 'a Ventus' if supreme.draught_shaft >= 5 else 'an Athmos'

	air = str('{type} system is used for this draft.').format(type=air_type)

	if (supreme.environment.oil =='eal'):
		rubber = 'FKM-EAL'
	elif pv > 4:
		rubber = 'FKM'
	else:
		rubber = 'NBR'

	if supreme.fwd_seal:
		pv_fwd = (supreme.fwdSize / 1000) * decimal.Decimal(3.14) * (supreme.rpm / 60) * (supreme.draught_shaft / 10)

		if (supreme.environment.oil =='eal'):
			rubber_fwd = 'FKM-EAL'
		elif pv_fwd > 4:
			rubber_fwd = 'FKM'
		else:
			rubber_fwd = 'NBR'

	else:
		pv_fwd = 0
		rubber_fwd = 'none' 

	sizeaft = findCorrectSize(supreme.aftSize)

	return render(request, 'sealadvisor2/supreme.html', { 'advise': supreme, 'pv':round(pv,1), 'air':air, 'rubber': rubber, 'pv_fwd': round(pv_fwd,1),'rubber_fwd':rubber_fwd, 'sizeaft':sizeaft })