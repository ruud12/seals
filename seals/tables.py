import django_tables2 as tables 
from seals.models import Seal
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django_tables2.utils import A

class SealTable(tables.Table):

	size = tables.Column()
	installedInVessel = tables.URLColumn()
	contact = tables.Column(empty_values=())
	company = tables.Column(empty_values=())
	id = tables.LinkColumn()

	def render_company(self,record):
		return record.installedInVessel.company

	def render_contact(self, record):
		return record.installedInVessel.contactPerson

	def render_installedInVessel(self, record):
		return str('{name} ({id})').format(name=record.installedInVessel, id=record.installedInVessel.id)

	def render_size(self, record):
		return str('{size} mm').format(size=record.size) 

	class Meta:
		model = Seal
		sequence = ('...','contact','company')

