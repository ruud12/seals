from django.shortcuts import render
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
	return render(request, 'seals/detail.html', {})