from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from erp.tables import componentTable, partsTable
from datetime import datetime


# Create your views here.

from erp.models import Seal, Company, sealComponent, Part, serviceReport, sealComponent, confirmComponentChange, Vessel, Mechanic, partMaterial, partCategory
from erp import forms

def index(request):
	seals = Seal.objects.all()
	companies = Company.objects.all()
	vessels = Vessel.objects.all()
	mechanics = Mechanic.objects.all()
	categories = partCategory.objects.all()
	materials = partMaterial.objects.all()

	return render(request, 'erp/index.html', {'seals':seals, 'companies':companies,'vessels':vessels, 'mechanics':mechanics, 'categories':categories,'materials':materials })



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


def addVessel(request):
	if request.method=="POST":
		form = forms.addVesselForm(request.POST)

		if form.is_valid():
			newVessel = form.save()

			return redirect('erp:index')

	else:
		form = forms.addVesselForm()

	return render(request, 'erp/simple_form.html', {'form': form, 'submit':'Create new vessel', 'title':'Add vessel'})


def editVessel(request, vessel_id):
	vessel = get_object_or_404(Vessel, pk=vessel_id)

	if request.method == 'POST':
		form = forms.addVesselForm(request.POST, instance = vessel)

		if form.is_valid():
			form.save()

			return redirect('erp:index')

	else:
		form = forms.addVesselForm(initial={'name':vessel.name, 'company':vessel.company.id })

	return render(request, 'erp/simple_form.html', {'form':form,'submit':'Save vessel','title':'Edit vessel'})


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

	return render(request, 'erp/simple_form.html', {'form':form, 'title':'Add service report','submit':'Add report'})


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
	material = get_object_or_404(Material, pk=mechanic_id)

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
	category = get_object_or_404(Category, pk=category_id)

	if request.method == 'POST':
		form = forms.addCategoryForm(request.POST, instance = category)

		if form.is_valid():
			form.save()

			return redirect('erp:index')

	else:
		form = forms.addCategoryForm(initial={'name':category.name })

	return render(request, 'erp/simple_form.html', {'form':form,'submit':'Save category','title':'Edit category'})

# inches to points
def itp(inch): 
	return inch * 72



def exportReportAsPDF(request, report_id):
	report = get_object_or_404(serviceReport, pk=report_id)


	# A4 paper is 8.3 by 11.7 inches
	# 1 point is equal to 1/72 inch
	# Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="report.pdf"'

	# Create the PDF object, using the response object as its "file."
	p = canvas.Canvas(response)
	width = 8.3
	height = 11.7


	mechanics = ([mechanic.first_name + " " + mechanic.last_name for mechanic in report.mechanics.all()])
	# Draw things on the PDF. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.
	p.drawString(itp(1), itp(10), report.name)
	p.drawString(itp(1), itp(9.5), report.date.strftime('Date: %d, %b %Y'))
	p.drawString(itp(1), itp(9), ", ".join(mechanics))

	# Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	return response