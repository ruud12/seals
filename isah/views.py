from django.shortcuts import render, get_object_or_404, redirect, render_to_response, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.http import HttpResponse, Http404
from django.template import RequestContext
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def index(request):
	return render(request, 'isah/index.html')
