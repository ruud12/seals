from django import forms
from servicerapportage.models import LS
from dal import autocomplete

class LSselectform(forms.Form):
    ls = forms.ModelChoiceField(
            queryset = LS.objects.all(),
            widget = autocomplete.ModelSelect2(
                url = 'index')
    )

    class Meta:
        fields = ('__all__')
