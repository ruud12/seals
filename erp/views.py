from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponseRedirect
from erp.tables import componentTable, partsTable

# Create your views here.

from erp.models import Seal, Company, sealComponent, Part, serviceReport, sealComponentChange, sealComponent
from erp import forms

def index(request):
	seals = Seal.objects.all()
	companies = Company.objects.all()

	return render(request, 'erp/index.html', {'seals':seals, 'companies':companies})



def viewAllParts(request):
	parts = Part.objects.all()

	table = partsTable(parts)

	return render(request, 'erp/viewAllParts.html', {'table':table})


def addPart(request):

	if request.method == "POST":
		form = forms.addPartForm(request.POST)

		if form.is_valid():
			newPart = form.save()

			return redirect('erp:viewAllParts')
	else:
		form = forms.addPartForm()

	return render(request,'erp/simple_form.html', {'form':form,'title':'Add part', 'submit':'Create part'})


def editPart(request, part_id):
	part = get_object_or_404(Part, pk=part_id)

	if request.method == "POST":
		form = forms.addPartForm(request.POST, instance=part)

		if form.is_valid():
			newPart = form.save()

			return redirect('erp:viewAllParts')
	else:
		form = forms.addPartForm(initial={'number':part.number,'category':part.category.id,'size':part.size,'name':part.name,'description':part.description,'material':part.material.id})

	return render(request,'erp/simple_form.html', {'form':form,'title':'Edit part', 'submit':'Save part'})




def viewSeal(request, seal_id):
	seal = get_object_or_404(Seal, pk=seal_id)
	parts = sealComponent.objects.filter(seal_id=seal_id)
	reports = serviceReport.objects.filter(seal_id=seal_id)
	table = componentTable(parts)



	return render(request, 'erp/viewSeal.html', {'seal':seal, 'parts':parts, 'table': table, 'reports':reports })



def addSeal(request):

	if request.method=='POST':
		form = forms.addSealForm(request.POST)

		if form.is_valid():
			newSeal = form.save()

			return redirect('erp:index')

	else:
		form = forms.addSealForm()

	return render(request, 'erp/seal.html', {'form':form, 'submit':'Create new seal object','title':'Add new seal'})



def editSeal(request, seal_id):
	seal = get_object_or_404(Seal, pk=seal_id)

	if request.method=='POST':
		form = forms.addSealForm(request.POST, instance = seal)

		if form.is_valid():
			form.save()

			return redirect('erp:viewSeal', seal_id)

	else:
		form = forms.addSealForm(initial={'x_number':seal.x_number, 'size':seal.size,'company':seal.company.id,'seal_type':seal.seal_type})

	return render(request, 'erp/seal.html', {'form':form, 'submit':'Save seal','title':'Edit seal'})


def addComponentToSeal(request, seal_id):
	seal = get_object_or_404(Seal, pk=seal_id)
	size = seal.size

	if request.method == 'POST':
		form = forms.addComponentToSealForm(request.POST,size=size)

		if form.is_valid():
			newComponent = form.save(commit=False)
			newComponent.seal = seal
			newComponent.save()

			return redirect('erp:viewSeal', seal_id)

	else:
		form = forms.addComponentToSealForm(size=size)

	return render(request, 'erp/simple_form.html', {'form':form, 'submit':'Add component to seal','title':'Add component'})



def addCompany(request):
	if request.method=="POST":
		form = forms.addCompanyForm(request.POST)

		if form.is_valid():
			newCompany = form.save()

			return redirect('erp:index')

	else:
		form = forms.addCompanyForm()

	return render(request, 'erp/company.html', {'form': form, 'submit':'Create new company', 'title':'Add new company'})


def editCompany(request, company_id):
	company = get_object_or_404(Company, pk=company_id)

	if request.method == 'POST':
		form = forms.addCompanyForm(request.POST, instance = company)

		if form.is_valid():
			form.save()

			return redirect('erp:index')

	else:
		form = forms.addCompanyForm(initial={'name':company.name })

	return render(request, 'erp/company.html', {'form':form,'submit':'Save company','title':'Edit company'})


def addServiceReport(request, seal_id):
	seal = get_object_or_404(Seal, pk=seal_id)

	if request.method == "POST":
		form = forms.addServiceReportForm(request.POST, seal_id=seal_id)

		if form.is_valid():
			newServiceReport = form.save(commit=False)
			newServiceReport.seal = seal
			newServiceReport.save()
			form.save_m2m()



			return redirect('erp:viewSeal', seal_id)

	else:
		form = forms.addServiceReportForm(seal_id=seal_id)

	return render(request, 'erp/simple_form.html', {'form':form, 'title':'Add service report','submit':'Add report'})


def checkComponentChange(request,seal_id,part_id):

	seal = get_object_or_404(Seal, pk=seal_id)
	part = get_object_or_404(Part, pk=part_id)

	form = forms.sealComponentChangeForm()

	return render(request,'erp/simple_form.html', {'form':form, 'title':'Check part replacement','submit':'Save'})