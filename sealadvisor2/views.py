
from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponseRedirect
from sealadvisor2 import forms
from sealadvisor2.models import supremeAdvise, AftSealOptions, environmentalOptions, FwdSealOptions
from erp.models import Company
import bisect, decimal
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import json

def determine_aft_execution(aft):
    execution = ""

#   if aft.linerCentering == 'shaft':
#       execution = execution + "A"

    if aft.hml:
        execution = execution + "C"
    if aft.distanceRing:
        execution = execution + "D"
    if aft.oring:
        execution = execution + "F"
    if aft.dirtBarrier:
        execution = execution + "L"
    if aft.anode:
        execution = execution + "P"

    execution = ''.join(sorted(execution))
    codes = (
        ("AA", "standard"),
        ("AB", "E"),
        ("AC", "F"),
        ("AD", "CFL"),
        ("AE", "D"),
        ("AF", "CDN"),
        ("AG", "nvt"),
        ("AH", "DL"),
        ("AJ", "N"),
        ("AK", "CL"),
        ("AL", "DF"),
        ("AM", "EF"),
        ("AN", "DE"),
        ("AO", "FL"),
        ("AP", "C"),
        ("AQ", "BE"),
        ("AR", "CN"),
        ("AS", "FW"),
        ("AT", "AEFL"),
        ("AU", "CDL"),
        ("AV", "CD"),
        ("AW", "DLN"),
        ("AX", "L"),
        ("AY", "BEF"),
        ("AZ", "CLN"),
        ("BA", "DN"),
        ("BB", "C2DN"),
        ("BC", "CELN"),
        ("BD", "CF"),
        ("BE", "AEF"),
        ("BF", "DFL"),
        ("BG", "ACEFL"),
        ("BH", "ADELZ"),
        ("BJ", "CNP"),
        ("BK", "LN"),
        ("BL", "LNP"),
        ("BM", "CLNP"),
        ("BN", "DEF"),
        ("BP", "FN"),
        ("BQ", "FLNP"),
        ("BR", "EL"),
        ("BS", "ACDFL"),
        ("BT", "ACDEFLM"),
        ("BU", "ADF"),
        ("BV", "ADFL"),
        ("BW", "ACEFLM"),
        ("BX", "ACELZ"),
        ("BY", "EFN"),
        ("BZ", "P"),
        ("CA", "AEFLN"),
        ("CB", "DEFN"),
        ("CC", "DFLN"),
        ("CD", "DEFLN"),
        ("CE", "EFNP"),
        ("CF", "AF"),
        ("CG", "ACDLZ"),
        ("CH", "CEN"),
        ("CJ", "EFL"),
        ("CK", "CFN"),
        ("CL", "CFLN"),
        ("CM", "ACFLN"),
        ("CN", "CENZ"),
        ("CP", "CLMN"),
        ("CQ", "CEFN"),
        ("CR", "CEFLN"),
        ("CS", "DEL "),
        ("CT", "CE"),
        ("CU", "AEFN"),
        ("CV", "DLNP"),
        ("CW", "ACEFLMPV"),
        ("CX", "AEFZ"),
        ("CY", "EN"),
        ("CZ", "DFN"),
        ("DA", "CEFL"),
        ("DB", "ACDF"),
        ("DC", "NP"),
        ("DD", "AEFLNPV"),
        ("DE", "CEL"),
        ("DF", "AZ"),
        ("DG", "CDFL"),
        ("DH", "DELN"),
    )

    print(execution)

    for x in codes:
        if x[1] == execution:
            execution_code = x[0]
            break
        else:
            execution_code = "??"
    if not execution_code:
        execution_code = "??"

    return {"execution": execution, 'code': execution_code }

def whichAirType(draught):
    return 'ventus' if draught > 4 else 'athmos'

def findCorrectSize(shaft_diameter):
    # check for the closest liner value taking into account a 1 cm liner thickness
    available_sizes = [155,170,190,200,220,240,260,280,300,330,355,380,400,420,450,480,500,530,560,600,630,670,710,750,800,850]

    liners = (
        (155,46260651,158,104,213,128,13,8),
        (170,46260652,173,140,233,128,13,8),
        (190,46260653,193,155,253,128,15,8),
        (200,46260654,203,175,263,128,15,8),
        (220,46260655,223,185,283,128,15,8),
        (240,46260656,243,203,303,138,15,10),
        (260,46260657,263,223,323,138,15,10),
        (280,46260658,283,243,353,138,18,10),
        (300,46260659,303,259,373,143,18,12),
        (330,46260660,333,279,403,143,18,12),
        (355,46260661,358,309,433,158,18,12),
        (380,46260662,383,332,463,158,18,12),
        (400,46260663,403,357,483,158,23,12),
        (420,46260664,423,375,503,158,23,12),
        (450,46260665,453,395,533,158,23,12),
        (480,46260666,483,421,563,158,23,12),
        (500,46260667,503,451,583,158,23,12),
        (530,46260668,533,470,613,158,23,12),
        (560,46260669,563,495,653,168,23,12),
        (600,46260670,603,525,703,168,23,12),
        (630,46260671,633,555,733,183,28,12),
        (670,46260672,673,585,773,198,28,12),
        (710,46260673,713,625,833,213,28,15),
        (750,46260674,753,665,873,213,28,15),
        (800,46260675,803,705,913,213,33,15),
        (850,46260676,853,745,963,213,33,15)
    )

    for x in range(0,len(liners)-1):
        if shaft_diameter > liners[x][3] and shaft_diameter <= liners[x+1][3]:
            available_size = liners[x][0]
            break
        else:
            available_size = 0

    print(available_size)
    # n = bisect.bisect_left(available_sizes,shaft_diameter+10)
    # return available_sizes[n]

    return available_size



def getTabs(advise):

    tabs = []
    tabs.append({'key':'General information', 'href': redirect('sealadvisor2:supremeEdit', advise.id).url})

    if advise.aft:
        tabs.append({'key':'Aft seal', 'href': redirect('sealadvisor2:supremeAftEdit', advise.id, advise.aft.id).url})

    if advise.fwd:
        tabs.append({'key':'Forward seal', 'href': redirect('sealadvisor2:supremeFwdEdit', advise.id, advise.fwd.id).url})

    return tabs



def index(request):
    advises = supremeAdvise.objects.all()
    companies = Company.objects.all()

    return render(request, 'sealadvisor2/index.html', {'advises': advises, 'companies':companies})


def salesType(request):

    if request.method == "POST":
        form = forms.supremeSalesTypeForm(request.POST)
        if form.is_valid():
            
            return redirect('sealadvisor2:supreme')

    else:
        form = forms.supremeSalesTypeForm()

    return render(request, 'sealadvisor2/simple_form.html', {'form':form, 'title': 'Choose sales type..', 'submit':'Next','cancel':'index' })


def supreme(request):
    if request.method == "POST":
        form = forms.supremeWizard(request.POST)
        if form.is_valid():
            newAdvise = form.save(commit=False)

            if newAdvise.application.key != 'sterntube':
                newAdvise.aft_seal = True

            try:
                company = Company.objects.get(name__iexact=form.cleaned_data['company_autocomplete'])
            except ObjectDoesNotExist:
                company = Company.objects.create(name=form.cleaned_data["company_autocomplete"])

            newAdvise.company = company

            newAdvise.save()


            return redirect('sealadvisor2:supremeEnvironment', newAdvise.id)
            


    else:
        form = forms.supremeWizard()

    tabs = {}

    return render(request, 'sealadvisor2/seal_information.html', {'form':form, 'title': "Add Supreme advise", 'submit':'Next','air':False, 'tabs':tabs})




def supremeEdit(request, supreme_id):
    supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

    if request.method == "POST":
        form = forms.supremeWizard(request.POST, instance=supreme)
        if form.is_valid():
            supreme = form.save(commit=False)

            if not supreme.aft_seal and supreme.aft:
                aft = get_object_or_404(AftSealOptions, pk = supreme.aft.id)
                supreme.aft = None
                aft.delete()

            if not supreme.fwd_seal and supreme.fwd:
                fwd = get_object_or_404(FwdSealOptions, pk = supreme.fwd.id)
                supreme.fwd = None
                fwd.delete()

            supreme.save()

            
            if (not supreme.aft) and (supreme.aft_seal):
                return redirect('sealadvisor2:supremeAft',supreme_id)
            elif (not supreme.fwd) and supreme.fwd_seal:
                return redirect('sealadvisor2:supremeFwd',supreme_id)
            elif (not supreme.environment):
                return redirect('sealadvisor2:supremeEnvironment',supreme_id)
            else:
                return redirect('sealadvisor2:supremeOverview',supreme_id)

    else:
        if supreme.typeApproval:
            form = forms.supremeWizard(initial={'company_autocomplete': supreme.company.name, 'vgp': supreme.vgp, 'aft_build_in_length': supreme.aft_build_in_length, 'application': supreme.application.id, 'cpp_fpp': supreme.cpp_fpp, 'fwd_seal': supreme.fwd_seal, 'aft_seal': supreme.aft_seal, 'aftSize': supreme.aftSize, 'fwdSize': supreme.fwdSize, 'rpm': supreme.rpm, 'draught_shaft': supreme.draught_shaft, 'typeApproval': supreme.typeApproval.id,'linerCentering':supreme.linerCentering , 'number_of_shafts':supreme.number_of_shafts})
        else:
            form = forms.supremeWizard(initial={'company_autocomplete': supreme.company.name, 'vgp': supreme.vgp, 'aft_build_in_length': supreme.aft_build_in_length, 'application': supreme.application.id, 'cpp_fpp': supreme.cpp_fpp, 'fwd_seal': supreme.fwd_seal, 'aft_seal': supreme.aft_seal, 'aftSize': supreme.aftSize, 'fwdSize': supreme.fwdSize, 'rpm': supreme.rpm, 'draught_shaft': supreme.draught_shaft, 'linerCentering':supreme.linerCentering, 'number_of_shafts':supreme.number_of_shafts})


    return render(request, 'sealadvisor2/add_supreme.html', {'form':form, 'title': "Edit Supreme advise", 'submit':'Save','extra':True, 'air':False})


def supremeFwd(request, supreme_id):
    supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

    if request.method == "POST":
        form = forms.supremeFwdForm(request.POST)
        if form.is_valid():
            fwdOptions = form.save()
            supreme.fwd = fwdOptions
            supreme.save()

            if (not supreme.aft) and supreme.aft_seal:
                return redirect('sealadvisor2:supremeAft', supreme_id)
            if (not supreme.environment):
                return redirect('sealadvisor2:supremeEnvironment', supreme_id)
            else:
                return redirect('sealadvisor2:supremeOverview', supreme_id)
            # return redirect('sealadvisor2:supremeEnvironment', supreme_id)

    else:
        form = forms.supremeFwdForm()



    tabs = getTabs(supreme)

    return render(request, 'sealadvisor2/fwd.html', {'form':form, 'title': 'Fwd seal options','submit':'Next','air':False,'extra':False,  'tabs': tabs})


def supremeFwdEdit(request, supreme_id, fwd_id):
    supreme = get_object_or_404(supremeAdvise, pk=supreme_id)
    fwd = get_object_or_404(FwdSealOptions, pk=fwd_id)

    if request.method == "POST":
        form = forms.supremeFwdForm(request.POST, instance=fwd)
        if form.is_valid():
            fwdOptions = form.save()

            if not supreme.environment:
                return redirect('sealadvisor2:supremeEnvironment', supreme_id)
            else:
                return redirect('sealadvisor2:supremeOverview', supreme_id)

    else:
        form = forms.supremeFwdForm(initial={'ocr':fwd.ocr, 'fkm':fwd.fkm})

    return render(request, 'sealadvisor2/fwd.html', {'form':form, 'title': 'Edit forward seal options','submit':'Save','air':False,'extra':False })




def supremeAft(request, supreme_id):
    supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

    if request.method == "POST":
        form = forms.supremeAftForm(request.POST)
        if form.is_valid():
            aftOptions = form.save()
            supreme.aft = aftOptions
            supreme.save()

            print (supreme.fwd_seal)

            if (not supreme.fwd) and supreme.fwd_seal:
                return redirect('sealadvisor2:supremeFwd', supreme_id)
            if (not supreme.environment):
                return redirect('sealadvisor2:supremeEnvironment', supreme_id)
            else:
                return redirect('sealadvisor2:supremeOverview', supreme_id)

    else:
        size = supreme.aftSize if supreme.aftSize else supreme.fwdSize
        if size > 600:
            form = forms.supremeAftForm(initial={'oring': True})
        else:
            form = forms.supremeAftForm()

    tabs = getTabs(supreme)

    return render(request, 'sealadvisor2/aft.html', {'form':form, 'title': 'Aft seal options','submit':'Next','air':False,'extra':False, 'tabs': tabs })



def supremeAftEdit(request, supreme_id, aft_id):
    supreme = get_object_or_404(supremeAdvise, pk=supreme_id)
    aft = get_object_or_404(AftSealOptions, pk=aft_id)

    if request.method == "POST":
        form = forms.supremeAftForm(request.POST, instance=aft)
        if form.is_valid():
            aftOptions = form.save()

            if not supreme.fwd and supreme.fwd_seal:
                return redirect('sealadvisor2:supremeFwd', supreme_id)
            elif not supreme.environment:
                return redirect('sealadvisor2:supremeEnvironment', supreme_id)
            else:
                return redirect('sealadvisor2:supremeOverview', supreme_id)

    else:
        form = forms.supremeAftForm(initial={'anode': aft.anode, 'seaguard':aft.seaguard, 'oring': aft.oring, 'distanceRing':aft.distanceRing, 'dirtBarrier': aft.dirtBarrier,'wireWinders':aft.wireWinders,'netCutters': aft.netCutters, 'hastelloy': aft.hastelloy})

    return render(request, 'sealadvisor2/aft.html', {'form':form, 'title': 'Edit aft seal options','submit':'Save','air':False})







def supremeEnvironment(request, supreme_id):
    supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

    if supreme.aft_seal:
        size = supreme.aftSize
    else:
        size = supreme.fwdSize

    pv = (size / 1000) * decimal.Decimal(3.14) * (supreme.rpm / 60) * (supreme.draught_shaft / 10)
    air_type= 'Ventus' if supreme.draught_shaft >= 5 else 'Athmos'

    if request.method == 'POST':
        form = forms.supremeEnvironmentForm(request.POST)
        if form.is_valid():
            environmentalOptions = form.save()
            supreme.environment = environmentalOptions
            supreme.save()

            # return redirect('sealadvisor2:supremeOverview', supreme_id)

            if (supreme.aft_seal) and not supreme.aft:
                return redirect('sealadvisor2:supremeAft',supreme.id)
            elif not supreme.fwd and supreme.fwd_seal:
                return redirect('sealadvisor2:supremeFwd', supreme.id)
            else:
                return redirect('sealadvisor2:supremeOverview', supreme.id)


    else:

        if supreme.aft:
            form = forms.supremeEnvironmentForm(initial={'air':supreme.aft.air, 'vgp': supreme.vgp})
        else:
            form = forms.supremeEnvironmentForm(initial={'vgp': supreme.vgp})

    tabs = getTabs(supreme)
    pv = round(pv,1)

    return render(request, 'sealadvisor2/environment.html', {'form':form, 'title': 'Environmental information','air_type':air_type,'pv':pv,'submit':'Next','air':True, 'tabs': tabs})


def supremeEnvironmentEdit(request, supreme_id, env_id):
    supreme = get_object_or_404(supremeAdvise, pk=supreme_id)
    env = get_object_or_404(environmentalOptions, pk=env_id)

    if supreme.aft:
        size = supreme.aftSize
    else:
        size = supreme.fwdSize


    pv = (size / 1000) * decimal.Decimal(3.14) * (supreme.rpm / 60) * (supreme.draught_shaft / 10)
    air_type= 'Ventus' if supreme.draught_shaft >= 5 else 'Athmos'

    if request.method == 'POST':
        form = forms.supremeEnvironmentForm(request.POST, instance = env)
        if form.is_valid():
            form.save()

            return redirect('sealadvisor2:supremeOverview', supreme_id)

    else:
        form = forms.supremeEnvironmentForm(initial = {'vgp':env.vgp, 'oil': env.oil, 'oilType': env.oilType, 'air': env.air})

    return render(request, 'sealadvisor2/environment.html', {'form':form, 'title': 'Environmental information','air_type':air_type,'pv':pv,'submit':'Save','air':True})






def supremeOverview(request, supreme_id):
    supreme = get_object_or_404(supremeAdvise, pk=supreme_id)

    if supreme.aft:
        size = supreme.aftSize
    elif supreme.fwd:
        size = supreme.fwdSize
    else:
        size=300


    pv = decimal.Decimal(size / 1000) * decimal.Decimal(3.14) * (supreme.rpm / 60) * (supreme.draught_shaft / 10)
    air_type= 'Ventus' if supreme.draught_shaft >= 5 else 'Athmos'

    air = str('{type} system is used for this draft.').format(type=air_type)


    if (supreme.environment):
        if (supreme.environment.oil =='eal'):
            rubber = 'FKM-EAL'
        elif pv > 4:
            rubber = 'FKM'
        else:
            rubber = 'NBR'
    else:
        rubber = 'Depends on environmental options which are not filled in.'

    if supreme.fwd_seal:
        pv_fwd = (supreme.fwdSize / 1000) * decimal.Decimal(3.14) * (supreme.rpm / 60) * (supreme.draught_shaft / 10)

        if (supreme.environment.oil =='eal'):
            rubber_fwd = 'FKM-EAL'
        elif pv_fwd > 4:
            rubber_fwd = 'FKM'
        else:
            rubber_fwd = 'NBR'

    else:
        pv_fwd = 0
        rubber_fwd = 'none' 


    if supreme.aft_seal:
        sizeaft = findCorrectSize(size)
        execution = determine_aft_execution(supreme.aft)

        if supreme.application.key == 'sterntube':
            number = "X01"
        elif supreme.application.key =='thruster':
            number = "X40"

        number = number + str(sizeaft) + execution['code'] + str(supreme.aftSize) + "A"

        if supreme.application.key == 'sterntube':
            sealtype = 'STA'

            if supreme.aft.seaguard:
                sealtype = "SG"

        elif supreme.application.key =='thruster':
            sealtype = "TS4"

        if supreme.environment.air:
            sealtype = sealtype + " (" + air_type + ")"


    else:
        sizeaft = ''
        execution = ''
        number = ''
        sealtype = '' 







    return render(request, 'sealadvisor2/supreme.html', {'type':sealtype, 'advise': supreme, 'pv':round(pv,1), 'air':air, 'rubber': rubber, 'pv_fwd': round(pv_fwd,1),'rubber_fwd':rubber_fwd, 'sizeaft':sizeaft, 'execution': execution, 'number': number })








from erp.models import Company

class CompanyCreate(CreateView):
    model = Company
    template_name = "sealadvisor2/simple_form.html"
    fields = ['name'] 
    
    def get_context_data(self, **kwargs):
        context = super(CompanyCreate, self).get_context_data(**kwargs)
        context['submit'] = 'Save'
        context['title'] = "Create new company"
        context["cancel"] = "index"
        return context
    
    
class CompanyUpdate(UpdateView):
    model = Company
    template_name = "sealadvisor2/simple_form.html"
    fields = ["name"]

    def get_context_data(self, **kwargs):
        context = super(CompanyUpdate, self).get_context_data(**kwargs)
        context['submit'] = 'Save'
        context['title'] = "Edit company"
        context["cancel"] = "index"
        return context   
   

class CompanyDelete(DeleteView):
    model = Company
    template_name = "sealadvisor2/simple_form.html"

    def get_context_data(self, **kwargs):
        context = super(CompanyDelete, self).get_context_data(**kwargs)
        context['submit'] = 'Yes, delete'
        context['title'] = "Delete company?"
        context["cancel"] = "index"
        return context   
   


class AdviseDelete(DeleteView):
    model = supremeAdvise
    template_name = "sealadvisor2/simple_form.html"

    def get_context_data(self, **kwargs):
        context = super(AdviseDelete, self).get_context_data(**kwargs)
        context['submit'] = 'Yes, delete'
        context['title'] = "Delete advise?"
        context["cancel"] = "index"
        return context   








def get_companies(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        drugs = Company.objects.filter(name__icontains = q )[:20]
        results = []
        for drug in drugs:
            drug_json = {}
            drug_json['id'] = drug.id
            drug_json['label'] = drug.name
            drug_json['value'] = drug.name
            results.append(drug_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)






def CompanyDefaultsEdit(request, company_id):
    company = get_object_or_404(Company, pk=company_id)

    if not company.aft_defaults:
        aft_defaults = AftSealOptions.objects.create()
        company.aft_defaults = aft_defaults
        company.save()

    if not company.fwd_defaults:
        fwd_defaults = FwdSealOptions.objects.create()
        company.fwd_defaults = fwd_defaults
        company.save()

    if request.method == "POST":
        form = forms.CompanyEditForm(request.POST, instance=company, prefix='company')
        aftform = forms.supremeAftForm(request.POST, prefix='aft', instance=company.aft_defaults)
        fwdform = forms.supremeFwdForm(request.POST, prefix='fwd', instance=company.fwd_defaults)

        if form.is_valid() and aftform.is_valid() and fwdform.is_valid():
            form.save()
            aftform.save()
            fwdform.save()
            return redirect('sealadvisor2:companies')

    else:
        form = forms.CompanyEditForm(prefix='company', initial = {'aft_defaults':company.aft_defaults.id, 'fwd_defaults': company.fwd_defaults.id, 'name': company.name })

        if company.aft_defaults:
            initial={
                'anode': company.aft_defaults.anode, 
                'seaguard': company.aft_defaults.seaguard, 
                'oring': company.aft_defaults.oring, 
                'distanceRing': company.aft_defaults.distanceRing, 
                'dirtBarrier': company.aft_defaults.dirtBarrier,
                'wireWinders': company.aft_defaults.wireWinders,
                'netCutters': company.aft_defaults.netCutters, 
                'hastelloy': company.aft_defaults.hastelloy}
        else:
            initial = {}

        aftform = forms.supremeAftForm(prefix='aft', initial=initial)

        if company.fwd_defaults:
            initial={'ocr':company.fwd_defaults.ocr, 'fkm':company.fwd_defaults.fkm, 'hml':company.fwd_defaults.hml, 'high_pressure':company.fwd_defaults.high_pressure}
        else:
            initial = {}
        
        fwdform = forms.supremeFwdForm(prefix='fwd', initial=initial)

    # if company.aft_defaults:
    #     aft_defaults = get_object_or_404(AftSealOptions, pk=company.aft_defaults.id)
    # else:
    #     aft_defaults = AftSealOptions()


    return render(request, 'sealadvisor2/company_edit.html', {'form':form, 'title':'Edit company defaults', 'cancel':'index','fwdform':fwdform, 'aftform':aftform, 'submit':'Save'})



def Companies(request):
    companies = Company.objects.all()
    
    return render(request, 'sealadvisor2/companies.html', {'companies':companies,'title':'Companies'})

def SupremeAdvises(request):
    advises = supremeAdvise.objects.all()
    
    return render(request, 'sealadvisor2/advises.html', {'advises':advises,'title':'Supreme advises'})
