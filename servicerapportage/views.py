from django.shortcuts import render
from dal import autocomplete
# Create your views here.

from isah.models import LS

from servicerapportage.forms import ServiceReportForm

class LSautocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = LS.objects.all()

        if self.q:
            qs = qs.filter(LS_number__icontains=self.q)

        return qs


def ServiceReport(request):
    form = ServiceReportForm()
    
    return render(request, 'servicerapportage/crispy_form.html', { 'form' : form })
