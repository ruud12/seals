from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_tables2 import RequestConfig
from isah.tables import sealTable, sealTypeTable, sealSizeTable, sealCompanyTable, sealVesselTable
from isah.models import Seal, SealSize, SealType, SealCompany, SealVessel
from isah import forms
from sealadvisor2 import forms as sealadvisor2forms
from sealadvisor2.models import AftSealOptions, FwdSealOptions
from isah.filters import SealFilter


# Create your views here.


def index(request):
    filter = SealFilter(request.GET, queryset=Seal.objects.all())

class ExtraContext(object):
    extra_context = {}
    
    def get_context_data(self, **kwargs):
        context = super(ExtraContext, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class Delete(ExtraContext, DeleteView):
    pass

def index(request):
	return render(request, 'isah/index.html')


def sealOverview(request):
    filters = SealFilter(request.GET, queryset=Seal.objects.all())
    table = sealTable(filters.qs)
    RequestConfig(request).configure(table)

    return render(request, 'isah/simple_table.html', {'filters':filters, 'title':'Seals',"table": table, 'add_form':'SealCreateForm'})


def SealCreate(request):
    if request.method == "POST":
        form = forms.SealForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('isah:SealOverview')

    else:
        form = forms.SealForm()

    return render(request, 'isah/simple_form.html', {'form':form, 'title':'Create new seal','submit':'Create'})




def SealEdit(request, pk):
    seal = Seal.objects.get(pk=pk)

    if request.method == "POST":
        form = forms.SealForm(request.POST, instance = seal)

        if form.is_valid():
            form.save()

            return redirect('isah:SealOverview')
    else:
        initial={'seal_type':seal.seal_type, 'size': seal.size, 'serial_number': seal.serial_number, 'company': seal.company.id }

        if seal.vessel:
            initial['vessel'] = seal.vessel.id 


        form = forms.SealForm(initial = initial)

    return render(request, 'isah/simple_form.html', {'form':form, 'title':'Edit seal','submit':'Save'})




def SealSizeOverview(request):
    sizes = SealSize.objects.all().order_by('size')
    table = sealSizeTable(sizes)

    return render(request, 'isah/simple_table.html', {'table': table, 'title': 'Seal sizes', 'add_form': 'SealSizeCreateForm'})


def SealSizeCreate(request):
    if request.method == "POST":
        form = forms.SealSizeForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('isah:SealSizeOverview')

    else:
        form = forms.SealSizeForm()

    return render(request, 'isah/simple_form.html', {'form':form, 'title':'Create new size','submit':'Create'})
    

def SealSizeEdit(request, pk):
    size = SealSize.objects.get(pk=pk)

    if request.method == "POST":
        form = forms.SealSizeForm(request.POST, instance = size)

        if form.is_valid():
            form.save()

            return redirect('isah:SealSizeOverview')
    else:
        form = forms.SealSizeForm(initial={'size':size.size})

    return render(request, 'isah/simple_form.html', {'form':form, 'title':'Edit size','submit':'Save'})


def SealTypeOverview(request):
    types = SealType.objects.all().order_by('name')

    table = sealTypeTable(types)

    return render(request, 'isah/simple_table.html', {'title':'Seal types', 'table':table, 'add_form': 'SealTypeCreateForm'})



def SealTypeCreate(request):
    if request.method == "POST":
        form = forms.SealTypeForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('isah:SealTypeOverview')

    else:
        form = forms.SealTypeForm()

    return render(request, 'isah/simple_form.html', {'form':form, 'title':'Create new type','submit':'Create'})
    

def SealTypeEdit(request, pk):
    type = SealType.objects.get(pk=pk)

    if request.method == "POST":
        form = forms.SealTypeForm(request.POST, instance = type)

        if form.is_valid():
            form.save()

            return redirect('isah:SealTypeOverview')
    else:
        form = forms.SealTypeForm(initial={'name':type.name, 'description':type.description})

    return render(request, 'isah/simple_form.html', {'form':form, 'title':'Edit type','submit':'Save'})

    
def SealCompanyOverview(request):
    companies = SealCompany.objects.order_by('name')

    table = sealCompanyTable(companies)

    return render(request, 'isah/simple_table.html', {'table': table, 'title': 'Companies', 'add_form': 'SealCompanyCreateForm'})


def SealCompanyCreate(request):
    if request.method == "POST":
        form = forms.SealCompanyForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('isah:SealCompanyOverview')

    else:
        form = forms.SealCompanyForm()

    return render(request, 'isah/simple_form.html', {'form':form, 'title':'Create new company','submit':'Create'})
    

def SealCompanyEdit(request, pk):
    company = SealCompany.objects.get(pk=pk)

    if request.method == "POST":
        form = forms.SealCompanyForm(request.POST, instance = company)

        if form.is_valid():
            form.save()

            return redirect('isah:SealCompanyOverview')
    else:
        form = forms.SealCompanyForm(initial={})

    return render(request, 'isah/simple_form.html', {'form':form, 'title':'Edit company','submit':'Save'})





def SealCompanyCreate2(request):

    if request.method == "POST":
        form = forms.SealCompanyForm(request.POST, prefix='company') # instance=company,
        aftform = sealadvisor2forms.supremeAftForm(request.POST, prefix='aft') # , instance=company.aft_preferences
        fwdform = sealadvisor2forms.supremeFwdForm(request.POST, prefix='fwd') # , instance=company.fwd_preferences

        if form.is_valid() and aftform.is_valid() and fwdform.is_valid():
            company = form.save(commit = False)

            aft_preferences = AftSealOptions.objects.create()
            company.aft_preferences = aft_preferences
            fwd_preferences = FwdSealOptions.objects.create()
            company.fwd_preferences = fwd_preferences

            company.save()

            aftform.save()
            fwdform.save()

            return redirect('isah:SealCompanyOverview')

    else:
        form = forms.SealCompanyForm(prefix='company')  # initial = {'aft_preferences':company.aft_preferences.id, 'fwd_preferences': company.fwd_preferences.id, 'name': company.name }
        aftform = sealadvisor2forms.supremeAftForm(prefix='aft') # , initial=initial
        fwdform = sealadvisor2forms.supremeFwdForm(prefix='fwd') # , initial=initial

    return render(request, 'isah/company.html', {'form':form, 'title':'Create company', 'cancel':'index','fwdform':fwdform, 'aftform':aftform, 'submit':'Create'})


def SealCompanyEdit2(request, pk):
    company = get_object_or_404(SealCompany, pk=pk)
    aft_preferences = get_object_or_404(AftSealOptions, pk=company.aft_preferences.id)
    fwd_preferences = get_object_or_404(FwdSealOptions, pk=company.fwd_preferences.id)

    if request.method == "POST":
        form = forms.SealCompanyForm(request.POST, prefix='company', instance=company)
        aftform = sealadvisor2forms.supremeAftForm(request.POST, prefix='aft', instance=aft_preferences)
        fwdform = sealadvisor2forms.supremeFwdForm(request.POST, prefix='fwd', instance=fwd_preferences)

        if form.is_valid() and aftform.is_valid() and fwdform.is_valid():
            company.save()
            aftform.save()
            fwdform.save()

            return redirect('isah:SealCompanyOverview')

    else:
        form = forms.SealCompanyForm(prefix='company', initial = {'aft_preferences':company.aft_preferences.id, 'fwd_preferences': company.fwd_preferences.id, 'name': company.name })

        initial = {
            'anode': company.aft_preferences.anode, 
            'seaguard': company.aft_preferences.seaguard, 
            'oring': company.aft_preferences.oring, 
            'distanceRing': company.aft_preferences.distanceRing, 
            'dirtBarrier': company.aft_preferences.dirtBarrier,
            'wireWinders': company.aft_preferences.wireWinders,
            'netCutters': company.aft_preferences.netCutters, 
            'hastelloy': company.aft_preferences.hastelloy
        }

        aftform = sealadvisor2forms.supremeAftForm(prefix='aft' , initial=initial)

        initial = {
            'ocr':company.fwd_preferences.ocr, 
            'fkm':company.fwd_preferences.fkm, 
            'hml':company.fwd_preferences.hml, 
            'high_pressure':company.fwd_preferences.high_pressure
        }
        
        fwdform = sealadvisor2forms.supremeFwdForm(prefix='fwd', initial=initial)




    return render(request, 'isah/company.html', {'form':form, 'title':'Edit company', 'cancel':'SealCompanyOverview','fwdform':fwdform, 'aftform':aftform, 'submit':'Save'})


def SealVesselOverview(request):
    vessels = SealVessel.objects.order_by('name')

    table = sealVesselTable(vessels)

    return render(request, 'isah/simple_table.html', {'title':'Vessels', 'table':table, 'add_form': 'SealVesselCreateForm'})



def SealVesselCreate(request):
    if request.method == "POST":
        form = forms.SealVesselForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('isah:SealVesselOverview')

    else:
        form = forms.SealVesselForm()

    return render(request, 'isah/simple_form.html', {'form':form, 'title':'Create new vessel','submit':'Create'})
    

def SealVesselEdit(request, pk):
    vessel = SealVessel.objects.get(pk=pk)

    if request.method == "POST":
        form = forms.SealVesselForm(request.POST, instance = vessel)

        if form.is_valid():
            form.save()

            return redirect('isah:SealVesselOverview')
    else:
        form = forms.SealVesselForm(initial={'name':vessel.name, 'imo_number': vessel.imo_number, 'company': vessel.company.id})

    return render(request, 'isah/simple_form.html', {'form':form, 'title':'Edit vessel','submit':'Save'})
