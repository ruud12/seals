from django.shortcuts import render, get_object_or_404
from django_tables2 import RequestConfig
from seals.models import Company, Seal, contactPerson, Vessel
from django.contrib.auth.models import User
from seals.tables import SealTable
from seals.filters import SealFilter

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


def vessel(request, company_id, vessel_id):

	vessels = Vessel.objects.filter(company=company_id).filter(pk=vessel_id)

	company = get_object_or_404(Company, pk=company_id)
	return render(request, 'seals/company.html', { 'company':company, 'vessels':vessels })
