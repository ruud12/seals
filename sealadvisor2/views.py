from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponseRedirect
from sealadvisor2 import forms
from sealadvisor2.models import supremeAdvise, AftSealOptions, environmentalOptions, FwdSealOptions
import bisect, decimal
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static

from django.http import HttpResponse



import os
from subprocess import Popen, PIPE
from tempfile import mkstemp
 
from django.http import HttpResponse, Http404
from django.template.loader import render_to_string
from django.template import RequestContext



def whichAirType(draught):
	return 'ventus' if draught > 4 else 'athmos'


def findCorrectSize(shaft_diameter):
	# check for the closest liner value taking into account a 1 cm liner thickness

	available_sizes = [110,125,155,175,200,225,260,330,355,440,600,720,800,900,1000]
	n = bisect.bisect_left(available_sizes,shaft_diameter+10)
	return available_sizes[n]



def getTabs(advise):

	tabs = []
	tabs.append({'key':'General information', 'href': redirect('sealadvisor2:supremeEdit', advise.id).url})

	if advise.aft:
		tabs.append({'key':'Aft seal', 'href': redirect('sealadvisor2:supremeAftEdit', advise.id, advise.aft.id).url})

	if advise.fwd:
		tabs.append({'key':'Forward seal', 'href': redirect('sealadvisor2:supremeFwdEdit', advise.id, advise.fwd.id).url})

	return tabs










def index(request):
	advises = supremeAdvise.objects.all()

	return render(request, 'sealadvisor2/index.html', {'advises': advises})


def supreme(request):
	if request.method == "POST":
		form = forms.supremeWizard(request.POST)
		if form.is_valid():
			newAdvise = form.save(commit=False)

			if newAdvise.application.key != 'sterntube':
				newAdvise.aft_seal = True

			newAdvise.save()


			
			if (newAdvise.aft_seal) and not newAdvise.aft:
				return redirect('sealadvisor2:supremeAft',newAdvise.id)
			elif not newAdvise.fwd and newAdvise.fwd_seal:
				return redirect('sealadvisor2:supremeFwd', newAdvise.id)
			else:
				return redirect('sealadvisor2:supremeEnvironment', newAdvise.id)

	else:
		form = forms.supremeWizard()

	tabs = {}

	return render(request, 'sealadvisor2/seal_information.html', {'form':form, 'title': "Add Supreme advise", 'submit':'Next','air':False, 'tabs':tabs})




def supremeEdit(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	if request.method == "POST":
		form = forms.supremeWizard(request.POST, instance=supreme)
		if form.is_valid():
			form.save()
			
			if (not supreme.aft) and (supreme.aft_seal):
				return redirect('sealadvisor2:supremeAft',supreme_id)
			elif (not supreme.fwd) and supreme.fwd_seal:
				return redirect('sealadvisor2:supremeAft',supreme_id)
			elif (not supreme.environment):
				return redirect('sealadvisor2:supremeEnvironement',supreme_id)
			else:
				return redirect('sealadvisor2:supremeOverview',supreme_id)

	else:
		if supreme.typeApproval:
			form = forms.supremeWizard(initial={'application': supreme.application.id, 'cpp_fpp': supreme.cpp_fpp, 'fwd_seal': supreme.fwd_seal, 'aft_seal': supreme.aft_seal, 'aftSize': supreme.aftSize, 'fwdSize': supreme.fwdSize, 'rpm': supreme.rpm, 'draught_shaft': supreme.draught_shaft, 'typeApproval': supreme.typeApproval.id })
		else:
			form = forms.supremeWizard(initial={'application': supreme.application.id, 'cpp_fpp': supreme.cpp_fpp, 'fwd_seal': supreme.fwd_seal, 'aft_seal': supreme.aft_seal, 'aftSize': supreme.aftSize, 'fwdSize': supreme.fwdSize, 'rpm': supreme.rpm, 'draught_shaft': supreme.draught_shaft })


	return render(request, 'sealadvisor2/add_supreme.html', {'form':form, 'title': "Edit Supreme advise", 'submit':'Save','air':False})


def supremeFwd(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	if request.method == "POST":
		form = forms.supremeFwdForm(request.POST)
		if form.is_valid():
			fwdOptions = form.save()
			supreme.fwd = fwdOptions
			supreme.save()

			return redirect('sealadvisor2:supremeEnvironment', supreme_id)

	else:
		form = forms.supremeFwdForm()



	tabs = getTabs(supreme)

	return render(request, 'sealadvisor2/seal_information.html', {'form':form, 'title': 'Fwd seal options','submit':'Next','air':False, 'tabs': tabs})


def supremeFwdEdit(request, supreme_id, fwd_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)
	fwd = get_object_or_404(FwdSealOptions, pk=fwd_id)

	if request.method == "POST":
		form = forms.supremeFwdForm(request.POST, instance=fwd)
		if form.is_valid():
			fwdOptions = form.save()

			if not supreme.environment:
				return redirect('sealadvisor2:supremeEnvironment', supreme_id)
			else:
				return redirect('sealadvisor2:supremeOverview', supreme_id)

	else:
		form = forms.supremeFwdForm(initial={'ocr':fwd.ocr, 'fkm':fwd.fkm})

	return render(request, 'sealadvisor2/seal_information.html', {'form':form, 'title': 'Edit forward seal options','submit':'Save','air':False})




def supremeAft(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	if request.method == "POST":
		form = forms.supremeAftForm(request.POST)
		if form.is_valid():
			aftOptions = form.save()
			supreme.aft = aftOptions
			supreme.save()

			print (supreme.fwd_seal)

			if (not supreme.fwd) and supreme.fwd_seal:
				return redirect('sealadvisor2:supremeFwd', supreme_id)
			if (not supreme.environment):
				return redirect('sealadvisor2:supremeEnvironment', supreme_id)
			else:
				return redirect('sealadvisor2:supremeOverview', supreme_id)

	else:
		size = supreme.aftSize if supreme.aftSize else supreme.fwdSize
		if size > 600:
			form = forms.supremeAftForm(initial={'oring': True})
		else:
			form = forms.supremeAftForm()

	tabs = getTabs(supreme)

	return render(request, 'sealadvisor2/seal_information.html', {'form':form, 'title': 'Aft seal options','submit':'Next','air':False, 'tabs': tabs })



def supremeAftEdit(request, supreme_id, aft_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)
	aft = get_object_or_404(AftSealOptions, pk=aft_id)

	if request.method == "POST":
		form = forms.supremeAftForm(request.POST, instance=aft)
		if form.is_valid():
			aftOptions = form.save()

			if not supreme.fwd and supreme.fwd_seal:
				return redirect('sealadvisor2:supremeFwd', supreme_id)
			elif not supreme.environment:
				return redirect('sealadvisor2:supremeEnvironment', supreme_id)
			else:
				return redirect('sealadvisor2:supremeOverview', supreme_id)

	else:
		form = forms.supremeAftForm(initial={'seaguard':aft.seaguard, 'oring': aft.oring, 'linerCentering':aft.linerCentering,'distanceRing':aft.distanceRing, 'dirtBarrier': aft.dirtBarrier,'wireWinders':aft.wireWinders,'netCutters': aft.netCutters, 'hastelloy': aft.hastelloy})

	return render(request, 'sealadvisor2/seal_information.html', {'form':form, 'title': 'Edit aft seal options','submit':'Save','air':False})







def supremeEnvironment(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	if supreme.aft:
		size = supreme.aftSize
	else:
		size = supreme.fwdSize

	pv = (size / 1000) * decimal.Decimal(3.14) * (supreme.rpm / 60) * (supreme.draught_shaft / 10)
	air_type= 'Ventus' if supreme.draught_shaft >= 5 else 'Athmos'

	if request.method == 'POST':
		form = forms.supremeEnvironmentForm(request.POST)
		if form.is_valid():
			environmentalOptions = form.save()
			supreme.environment = environmentalOptions
			supreme.save()

			return redirect('sealadvisor2:supremeOverview', supreme_id)

	else:

		if supreme.aft:
			form = forms.supremeEnvironmentForm(initial={'air':supreme.aft.air})
		else:
			form = forms.supremeEnvironmentForm()

	tabs = getTabs(supreme)


	return render(request, 'sealadvisor2/seal_information.html', {'form':form, 'title': 'Environmental information','air_type':air_type,'pv':pv,'submit':'Save','air':True, 'tabs': tabs})


def supremeEnvironmentEdit(request, supreme_id, env_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)
	env = get_object_or_404(environmentalOptions, pk=env_id)

	if supreme.aft:
		size = supreme.aftSize
	else:
		size = supreme.fwdSize


	pv = (size / 1000) * decimal.Decimal(3.14) * (supreme.rpm / 60) * (supreme.draught_shaft / 10)
	air_type= 'Ventus' if supreme.draught_shaft >= 5 else 'Athmos'

	if request.method == 'POST':
		form = forms.supremeEnvironmentForm(request.POST, instance = env)
		if form.is_valid():
			form.save()

			return redirect('sealadvisor2:supremeOverview', supreme_id)

	else:
		form = forms.supremeEnvironmentForm(initial = {'vgp':env.vgp, 'oil': env.oil, 'oilType': env.oilType, 'air': env.air})

	return render(request, 'sealadvisor2/seal_information.html', {'form':form, 'title': 'Environmental information','air_type':air_type,'pv':pv,'submit':'Save','air':True})






def supremeOverview(request, supreme_id):
	supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

	if supreme.aft:
		size = supreme.aftSize
	else:
		size = supreme.fwdSize


	pv = (size / 1000) * decimal.Decimal(3.14) * (supreme.rpm / 60) * (supreme.draught_shaft / 10)
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

	sizeaft = findCorrectSize(size)

	return render(request, 'sealadvisor2/supreme.html', { 'advise': supreme, 'pv':round(pv,1), 'air':air, 'rubber': rubber, 'pv_fwd': round(pv_fwd,1),'rubber_fwd':rubber_fwd, 'sizeaft':sizeaft })


def render_latex(request, template, dictionary, filename):
    # render latex template and vars to a string
    latex = render_to_string(template, dictionary, context_instance=None)
 
    # create a unique temorary filename
    fd, path = mkstemp(prefix="latex_", suffix=".pdf")
    folder, fname = os.path.split(path)
    jobname, ext = os.path.splitext(fname)  # jobname is just the filename without .pdf, it's what pdflatex uses
 
    # for the TOC to be built, pdflatex must be run twice, on the second run it will generate a .toc file
    for i in range(2):
        # start pdflatex, we can send the tex file from stdin, but the output file can only be saved to disk, not piped to stdout unfortunately/
        process = Popen(["pdflatex", "-output-directory", folder, "-jobname", jobname], stdin=PIPE, stdout=PIPE)  # piping stdout suppresses output messages
        process.communicate(latex)
 
    # open the temporary pdf file for reading.
    try:
        pdf = os.fdopen(fd, "rb")
        output = pdf.read()
        pdf.close()
    except OSError:
        raise Http404("Error generating PDF file")  # maybe we should use an http  500 here, 404 makes no sense
 
    # generate the response with pdf attachment
    response = HttpResponse(mimetype="application/pdf")
    response["Content-Disposition"] = "attachment; filename=" + filename
    response.write(output)
 
    # delete the pdf from temp directory, and other generated files ending on .aux and .log
    for ext in (".pdf", ".aux", ".log", ".toc", ".lof", ".lot", ".synctex.gz"):
        try:
            os.remove(os.path.join(folder, jobname) + ext)
        except OSError:
            pass
 
    # return the response
    return response
 
#### Actual Usage ####
 
def someview(request):
    return render_latex(request, "reports/test.tex", {"foo": "bar"}, filename="latex_test.pdf")