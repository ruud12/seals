from django.shortcuts import render

# Create your views here.

from erp.models import Seal, Company
from erp import forms

def index(request):
	seals = Seal.objects.all()

	return render(request, 'erp/index.html', {'seals':seals})


def addSeal(request):

	if request.method=='POST':
		form = forms.AddSealForm(request.POST)

		if form.is_valid():
			newSeal = form.save()

	else:
		form = forms.addSealForm()

	return render(request, 'erp/seal.html', {'form':form, 'submit':'Create new seal object','title':'Add new seal'})