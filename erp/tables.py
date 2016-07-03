import django_tables2 as tables 
from erp.models import Seal, sealComponent
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django_tables2.utils import A


class componentTable(tables.Table):

	number = tables.Column(verbose_name='#')

	class Meta:
		model = sealComponent
		attrs = {'class': 'bordered striped'}
		fields = ('number','part')