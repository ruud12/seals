from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django_tables2 import RequestConfig
from seals.models import Company, Seal, contactPerson, Vessel, Report
from django.contrib.auth.models import User
from seals.tables import SealTable
from seals.filters import SealFilter
from seals.forms import AddAction
from formtools.wizard.views import SessionWizardView

# Create your views here.


def index(request):

	# table = SealTable(Seal.objects.all())
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

def home(request):
	return render(request, 'seals/home.html')




