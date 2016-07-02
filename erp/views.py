from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponseRedirect

# Create your views here.

from erp.models import Seal, Company, sealComponent
from erp import forms

def index(request):
	seals = Seal.objects.all()
	companies = Company.objects.all()

	return render(request, 'erp/index.html', {'seals':seals, 'companies':companies})


def viewSeal(request, seal_id):
	seal = get_object_or_404(Seal, pk=seal_id)
	parts = sealComponent.objects.filter(seal_id=seal_id)

	return render(request, 'erp/viewSeal.html', {'seal':seal, 'parts':parts })



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

			return redirect('erp:index')

	else:
		form = forms.addSealForm(initial={'x_number':seal.x_number, 'size':seal.size,'company':seal.company.id,'seal_type':seal.seal_type})

	return render(request, 'erp/seal.html', {'form':form, 'submit':'Save seal','title':'Edit seal'})


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

