from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponseRedirect
from sealadvisor2 import forms
from sealadvisor2.models import supremeAdvise
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
	return render(request, 'sealadvisor2/index.html')


def supreme(request):

	if request.method == "POST":
		form = forms.supremeWizard(request.POST)
		if form.is_valid():
			newAdvise = form.save()
			
			return redirect('sealadvisor2:supremeAft',newAdvise.id)
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

