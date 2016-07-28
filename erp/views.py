from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from erp.tables import componentTable, partsTable
from datetime import datetime

# Create your views here.

from erp.models import Seal, Company, sealComponent, Part, serviceReport, sealComponent, confirmComponentChange, Vessel, Mechanic, partMaterial, partCategory, contactPerson
from erp import forms

def index(request):
	seals = Seal.objects.all()
	companies = Company.objects.all()
	vessels = Vessel.objects.all()
	mechanics = Mechanic.objects.all()
	categories = partCategory.objects.all()
	materials = partMaterial.objects.all()
	contacts = contactPerson.objects.all()

	return render(request, 'erp/index.html', {'seals':seals, 'companies':companies,'vessels':vessels, 'mechanics':mechanics, 'categories':categories,'materials':materials, 'contacts':contacts })



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
	changed_parts = confirmComponentChange.objects.filter(seal_id=seal_id)



	return render(request, 'erp/viewSeal.html', {'seal':seal, 'parts':parts, 'table': table, 'reports':reports, 'changes': changed_parts })



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
	old = seal

	if request.method=='POST':
		form = forms.addSealForm(request.POST, instance = seal)

		if form.is_valid():
			s = form.save()
			return redirect('erp:viewSeal', seal_id)

	else:
		form = forms.addSealForm(initial={'date_installed':seal.date_installed, 'x_number':seal.x_number, 'size':seal.size,'company':seal.company.id,'seal_type':seal.seal_type, 'vessel': seal.vessel.id})

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


def addVessel(request, company_id):
	if request.method=="POST":
		form = forms.addVesselForm(request.POST, company_id=company_id)

		if form.is_valid():
			newVessel = form.save()

			return redirect('erp:index')

	else:
		form = forms.addVesselForm(company_id=company_id, initial={'company': company_id })

	return render(request, 'erp/simple_form.html', {'form': form, 'submit':'Create new vessel', 'title':'Add vessel'})


def editVessel(request, vessel_id):
	vessel = get_object_or_404(Vessel, pk=vessel_id)

	if request.method == 'POST':
		form = forms.addVesselForm(request.POST, company_id = vessel.company.id, instance = vessel)

		if form.is_valid():
			form.save()

			return redirect('erp:index')

	else:
		form = forms.addVesselForm(company_id=vessel.company.id, initial={'name':vessel.name, 'company':vessel.company.id, 'imo': vessel.imo, 'contacts':[contact.id for contact in vessel.contacts.all()] })

	return render(request, 'erp/simple_form.html', {'form':form,'submit':'Save vessel','title':'Edit vessel'})



def addContactPerson(request):
	if request.method=="POST":
		form = forms.addContactPersonForm(request.POST)

		if form.is_valid():
			newContactPerson = form.save()

			return redirect('erp:index')

	else:
		form = forms.addContactPersonForm()

	return render(request, 'erp/simple_form.html', {'form': form, 'submit':'Create new contact person', 'title':'Add contact person'})


def editContactPerson(request, contact_id):
	contact = get_object_or_404(contactPerson, pk=contact_id)

	if request.method == 'POST':
		form = forms.addContactPersonForm(request.POST, instance = contact)

		if form.is_valid():
			form.save()

			return redirect('erp:index')

	else:
		form = forms.addContactPersonForm(initial={'first_name':contact.first_name, 'last_name':contact.last_name,'position':contact.position, 'company':contact.company.id })

	return render(request, 'erp/simple_form.html', {'form':form,'submit':'Save contact','title':'Edit contact'})



def addServiceReport(request, seal_id):
	seal = get_object_or_404(Seal, pk=seal_id)

	if request.method == "POST":
		form = forms.addServiceReportForm(request.POST, seal_id=seal_id)

		if form.is_valid():
			newServiceReport = form.save(commit=False)
			newServiceReport.seal = seal
			newServiceReport.save()
			form.save_m2m()

			servicereport = get_object_or_404(serviceReport, pk=newServiceReport.id)


			# create confirm objects for each changed part
			# for change in servicereport.parts_to_replace.all():
			# 	confirmComponentChange.objects.create(report=servicereport, old_part=change.part, new_part=change.part)

			return redirect('erp:viewSeal', seal_id)

	else:
		form = forms.addServiceReportForm(seal_id=seal_id)


	return render(request, 'erp/simple_form.html', {'form':form, 'title':'Add service report for '+seal.x_number,'submit':'Add report', 'seal':seal})


def checkComponentChange(request,seal_id, change_id):

	change = get_object_or_404(confirmComponentChangeForm, pk = change_id)

	if request.method == "POST":
		form = forms.confirmComponentChangeForm(request.POST, instance=change)

		if form.is_valid():
			form.save(update_fields=['new_part','old_part','confirm'])

			return redirect('erp:viewSeal', seal_id)

	form = forms.confirmComponentChangeForm(initial = {'old_part':change.old_part, 'new_part': change.new_part})

	return render(request,'erp/simple_form.html', {'form':form, 'title':'Check part replacement','submit':'Save'})



def addMechanic(request):
	if request.method=="POST":
		form = forms.addMechanicForm(request.POST)

		if form.is_valid():
			newMechanic = form.save()

			return redirect('erp:index')

	else:
		form = forms.addMechanicForm()

	return render(request, 'erp/simple_form.html', {'form': form, 'submit':'Create new mechanic', 'title':'Add mechanic'})


def editMechanic(request, mechanic_id):
	mechanic = get_object_or_404(Mechanic, pk=mechanic_id)

	if request.method == 'POST':
		form = forms.addMechanicForm(request.POST, instance = mechanic)

		if form.is_valid():
			form.save()

			return redirect('erp:index')

	else:
		form = forms.addMechanicForm(initial={'first_name':mechanic.first_name, 'last_name': mechanic.last_name })

	return render(request, 'erp/simple_form.html', {'form':form,'submit':'Save mechanic','title':'Edit mechanic'})


def addMaterial(request):
	if request.method=="POST":
		form = forms.addMaterialForm(request.POST)

		if form.is_valid():
			newMaterial = form.save()

			return redirect('erp:index')

	else:
		form = forms.addMaterialForm()

	return render(request, 'erp/simple_form.html', {'form': form, 'submit':'Create new material', 'title':'Add material'})

def editMaterial(request, material_id):
	material = get_object_or_404(partMaterial, pk=material_id)

	if request.method == 'POST':
		form = forms.addMaterialForm(request.POST, instance = material)

		if form.is_valid():
			form.save()

			return redirect('erp:index')

	else:
		form = forms.addMaterialForm(initial={'name':material.name })

	return render(request, 'erp/simple_form.html', {'form':form,'submit':'Save material','title':'Edit material'})





def addCategory(request):
	if request.method=="POST":
		form = forms.addCategoryForm(request.POST)

		if form.is_valid():
			newCategory = form.save()

			return redirect('erp:index')

	else:
		form = forms.addCategoryForm()

	return render(request, 'erp/simple_form.html', {'form': form, 'submit':'Create new category', 'title':'Add category'})


def editCategory(request, category_id):
	category = get_object_or_404(partCategory, pk=category_id)

	if request.method == 'POST':
		form = forms.addCategoryForm(request.POST, instance = category)

		if form.is_valid():
			form.save()

			return redirect('erp:index')

	else:
		form = forms.addCategoryForm(initial={'name':category.name })

	return render(request, 'erp/simple_form.html', {'form':form,'submit':'Save category','title':'Edit category'})









def exportReportAsPDF(request, report_id):
	from erp.printing import MyPrint
	from io import BytesIO

	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="reports.pdf"'

	buffer = BytesIO()

	report = get_object_or_404(serviceReport, pk=report_id)

	report = MyPrint(buffer, 'A4', report)

	pdf = report.export_report()

	response.write(pdf)

	return response


	


def addVesselCompany(request):

	if request.method == "POST":
		form = forms.selectCompany(request.POST)

		if form.is_valid():
			# do something
			print(form.cleaned_data['company'].id)

			company_id = form.cleaned_data['company'].id

			return redirect('erp:addVessel', company_id)

	else:
		form = forms.selectCompany()

	return render(request, 'erp/simple_form.html', { 'form': form, 'title':'Select company', 'submit': 'Next' })
