import django_tables2 as tables 
from isah.models import Seal
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django_tables2.utils import A




class sealTable(tables.Table):
    
    class Meta:
        model = Seal
        attrs = {'class':'bordered striped'}
        fields = ("size","seal_type", "serial_number", "created", "updated")
