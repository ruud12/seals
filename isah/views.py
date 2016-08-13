from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from isah.tables import sealTable
from isah.models import Seal


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
