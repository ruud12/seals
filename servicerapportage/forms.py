from django import forms
from isah.models import LS
from dal import autocomplete
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class LSselectform(forms.Form):
    ls = forms.ModelChoiceField(
            queryset = LS.objects.all(),
            widget = autocomplete.ModelSelect2(
                url = 'index')
    )

    class Meta:
        fields = ('__all__')


class ServiceReportForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ServiceReportForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.add_input(Submit('submit', 'Submit'))

    side = forms.TypedChoiceField(
            label = "Forward or aft seal",
            choices = ((1,'fwd', 2, 'aft')),
            widget = forms.RadioSelect,
            required = True,
    )

