from django.shortcuts import render

from seals.models import Company, Seal, contactPerson, Vessel
from django.contrib.auth.models import User


# Create your views here.


def index(request):

	seals = Seal.objects.all()
	return render(request, 'seals/index.html', { 'seals' : seals })