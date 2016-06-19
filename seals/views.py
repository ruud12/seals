from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django_tables2 import RequestConfig
from seals.models import Company, Seal, contactPerson, Vessel, Report
from django.contrib.auth.models import User
from seals.tables import SealTable
from seals.filters import SealFilter
from seals.forms import AddAction, AddReport, AddSeal, DeleteSeal, EditSeal, EditVessel, EditCompany, AddContact, EditContact
from formtools.wizard.views import SessionWizardView
from django.utils import timezone
from datetime import datetime

# Create your views here.


def index(request):
	filter = SealFilter(request.GET, queryset=Seal.objects.all())
	table = SealTable(filter.qs)
	RequestConfig(request).configure(table)

	return render(request, 'seals/index.html', { 'table' : table, 'filter': filter })

def detail(request, primary_key):
	seal = get_object_or_404(Seal, pk=primary_key)	
	return render(request, 'seals/detail.html', {'seal': seal})	

def company(request, company_id):
	company = get_object_or_404(Company, pk=company_id)
	vessels = Vessel.objects.filter(company=company_id)
	return render(request, 'seals/company.html', { 'company':company, 'vessels':vessels })


def vessel_detail(request, vessel_id):
	vessel = get_object_or_404(Vessel, pk=vessel_id)
	return render(request, 'seals/vessel_detail.html', { 'vessel': vessel })


def add_action(request, seal_id, report_id):
	if request.method == "POST":
		form = AddAction(request.POST)
		if form.is_valid():
			new_action = form.save(commit=False)
			new_action.relatedtoseal = get_object_or_404(Seal, pk=seal_id)
			new_action.relatedtoreport = get_object_or_404(Report, pk=report_id)
			new_action.save()
			return redirect('seals:detail', primary_key=seal_id)
	else:
		form = AddAction()

	report = get_object_or_404(Report, pk=report_id)
	seal = get_object_or_404(Seal, pk=seal_id)

	return render(request, 'seals/add_action.html', {'seal': seal, 'report': report, 'form':form})


def add_report(request, seal_id):
	seal = get_object_or_404(Seal, pk=seal_id)
	contact_choices = [[contact.id, contact] for contact in contactPerson.objects.filter(company =seal.installedinvessel.company)]

	if request.method == "POST":
		form = AddReport(request.POST)
		if form.is_valid():
			new_report = form.save(commit=False)
			new_report.relatedtoseal = get_object_or_404(Seal, pk=seal_id)
			new_report.save()
			return redirect('seals:detail', primary_key=seal_id)

	else:
		form = AddReport(choices=contact_choices)


	return render(request, 'seals/add_report.html', {'seal':seal, 'form':form})

def home(request):
	return render(request, 'seals/home.html')


def add_seal(request):
	if request.method == "POST":
		form = AddSeal(request.POST)
		if form.is_valid():
			new_seal = form.save(commit=False)
			new_seal.created = datetime.now()
			new_seal.save()
			return redirect('seals:detail', primary_key=new_seal.id)

	else:
		form = AddSeal()

	return render(request, 'seals/add_seal.html', {'form':form})

def delete(request, seal_id):
	seal = get_object_or_404(Seal, pk=seal_id)
	if request.method == "POST":
		form = DeleteSeal(request.POST, seal)
		if form.is_valid():
			seal.delete()
			return redirect('seals:index')
	else:
		form = DeleteSeal()
	return render(request, 'seals/delete.html', { 'seal':seal, 'form':form })





def edit(request, seal_id):
	seal = get_object_or_404(Seal, pk=seal_id)

	if request.method == "POST":
		form = EditSeal(request.POST, instance=seal)
		if form.is_valid():
			edit_seal = form.save(commit=False)
			edit_seal.created = seal.created
			edit_seal.id = seal.id

			edit_seal.save()
			return redirect('seals:detail', primary_key=seal.id)
	else:
		form = EditSeal(initial={'serial_number': seal.serial_number, 'size': seal.size, 'installedinvessel': seal.installedinvessel.pk, 'status': seal.status.pk})


	return render(request,'seals/edit.html', {'seal':seal, 'form':form})


def editVessel(request, vessel_id):
	vessel = get_object_or_404(Vessel, pk=vessel_id)

	if request.method == "POST":
		form = EditVessel(request.POST, instance=vessel)
		if form.is_valid():
			edit_vessel = form.save(commit=False)
			# edit_vessel.created = seal.created
			edit_vessel.id = vessel.id
			edit_vessel.save()

			return redirect('seals:vessel_detail', vessel_id=vessel.id)
	else:
		form = EditVessel(initial={'name':vessel.name, 'imo_number':vessel.imo_number,'company':vessel.company.pk, 'contact' : [c.pk for c in vessel.contact.all()]})


	return render(request,'seals/edit_vessel.html', {'vessel':vessel, 'form':form})


def editCompany(request, company_id):
	company = get_object_or_404(Company, pk=company_id)

	if request.method == "POST":
		form = EditCompany(request.POST, instance=company)
		if form.is_valid():
			edit_company = form.save(commit=False)
			# edit_vessel.created = seal.created
			edit_company.id = company.id
			edit_company.save()

			return redirect('seals:company', company_id=company.id)
	else:
		form = EditCompany(initial={'name':company.name,'street':company.street,'streetNumber':company.streetNumber,'city':company.city,'country':company.country.code})


	return render(request,'seals/edit_company.html', {'company':company, 'form':form})


def addContact(request, company_id):
	company = get_object_or_404(Company, pk=company_id)

	
	if request.method == "POST":
		form = AddContact(request.POST)

		if form.is_valid():
			new_contact = form.save(commit=False)
			new_contact.company = company
			new_contact.save()

			return redirect('seals:company', company_id=company.id)

	else:
		form = AddContact()


	return render(request, 'seals/add_contact.html', {'company':company, 'form':form})


def editContact(request, contact_id, company_id):
	contact = get_object_or_404(contactPerson, pk=contact_id)
	company = get_object_or_404(Company, pk=company_id)

	if request.method == "POST":
		form = EditContact(request.POST, instance=contact)

		if form.is_valid():
			updated_contact = form.save()

		return redirect('seals:company', company_id=company.id)

	else:
		form = EditContact(initial={'first_name':contact.first_name,'last_name':contact.last_name, 'position':contact.position,'phone_number':contact.phone_number,'company':contact.company.pk})

		return render(request, 'seals/edit_contact.html', {'contact':contact,'form':form})

def deleteContact(request, contact_id, ):
	contact = get_object_or_404(contactPerson, pk=contact_id)
	company_id = contact.company.id
	contact.delete()

	return redirect('seals:company', company_id=company_id)

