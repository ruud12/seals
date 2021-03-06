import django_tables2 as tables 
from erp.models import Seal, sealComponent, Part, Seal
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django_tables2.utils import A


class componentTable(tables.Table):

	number = tables.Column(verbose_name='#')
	partNumber = tables.Column(accessor='part.number')
	size = tables.Column(accessor='part.size')
	material = tables.Column(accessor='part.material')
	name = tables.Column(accessor='part.name')

	class Meta:
		model = sealComponent
		attrs = {'class': 'bordered striped'}
		fields = ('number','partNumber', 'name','size', 'status')

class partsTable(tables.Table):

	def render_edit(self, record):
		return mark_safe('<a href='+reverse("erp:editPart", args=[record.pk])+'>Edit</a>')

	edit = tables.LinkColumn('erp:editPart', args=[A('pk')], empty_values=())

	class Meta:
		model = Part
		attrs = {'class': 'bordered striped'}
		fields = ('name','category','material','number','size','edit')


class sealTable(tables.Table):
    
    class Meta:
        model = Seal
        attrs = {'class':'bordered striped'}
        fields = ("x_number" ,"seal_type", "size", "company", "vessel", "date_installed")
