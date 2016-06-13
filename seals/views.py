from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django_tables2 import RequestConfig
from seals.models import Company, Seal, contactPerson, Vessel, Report
from django.contrib.auth.models import User
from seals.tables import SealTable
from seals.filters import SealFilter
from seals.forms import AddAction, AddReport, AddSeal, DeleteSeal
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

def company(request, primary_key):
	company = get_object_or_404(Company, pk=primary_key)
	vessels = Vessel.objects.filter(company=primary_key)
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
			new_seal = form.save()
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