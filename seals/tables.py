import django_tables2 as tables 
from seals.models import Seal
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django_tables2.utils import A

class SealTable(tables.Table):

	size = tables.Column()
	contact = tables.Column(empty_values=(), verbose_name='Contact person(s)')


	company = tables.LinkColumn('seals:company', args=[A('installedinvessel.company.id')], accessor='installedinvessel.company', verbose_name='Company')
	installedinvessel = tables.LinkColumn('seals:vessel_detail', args=[A('installedinvessel.id')], accessor='installedinvessel')
	serial_number = tables.LinkColumn('seals:detail', args=[A('pk')])

	def render_contact(self, record):
		contacts = record.installedinvessel.contact.all()

		text = []

		for contact in contacts:
			text.append(str("{user} ({position})").format(user=contact,position=contact.position))

		return ", ".join(text)


	def render_size(self, record):
		return str('{size} mm').format(size=record.size) 

	class Meta:
		model = Seal
		sequence = ('serial_number','...')
		fields= ('serial_number', 'size', 'installedinvessel','company', 'contact')
		attrs = {'class': 'bordered striped'}


