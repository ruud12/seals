from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from isah.tables import sealTable, sealTypeTable, sealSizeTable
from isah.models import Seal, SealSize, SealType
from isah import forms


def index(request):
	return render(request, 'isah/index.html')


def sealOverview(request):
    seals = Seal.objects.all()
    table = sealTable(seals)
    
    return render(request, 'isah/sealOverview.html', {"table": table})



class ExtraContext(object):
    extra_context = {}
    
    def get_context_data(self, **kwargs):
        context = super(ExtraContext, self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context


class Create(ExtraContext, CreateView):
    pass

class Delete(ExtraContext, DeleteView):
    pass



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

    
#class ClassUpdate(UpdateView):
    #model = Certificate
    #template_name = "sealadvisor2/simple_form.html"
    #fields = ['key', 'bureau'] 

    #def get_context_data(self, **kwargs):
        #context = super(ClassUpdate, self).get_context_data(**kwargs)
        #context['submit'] = 'Save'
        #context['title'] = "Edit class"
        #context["cancel"] = "classOverview"
        #return context   

#class ClassDelete(DeleteView):
    #model = Certificate
    #template_name = "sealadvisor2/simple_form.html"

    #def get_context_data(self, **kwargs):
        #context = super(ClassDelete, self).get_context_data(**kwargs)
        #context['submit'] = 'Yes, delete'
        #context['title'] = "Delete class?"
        #context["cancel"] = "classOverview"
        #return context   
