import django_tables2 as tables 
from seals.models import Seal
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django_tables2.utils import A

class SealTable(tables.Table):

	size = tables.Column()
	installedInVessel = tables.URLColumn()

	serial_number = tables.LinkColumn('detail', args=[A('pk')])


	def render_size(self, record):
		return str('{size} mm').format(size=record.size) 

	class Meta:
		model = Seal

