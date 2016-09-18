from django.shortcuts import render
from dal import autocomplete
# Create your views here.

from isah.models import LS

class LSautocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        if self.q:
            qs = qs.filter(LS_number__icontains=self.q)

        return qs
