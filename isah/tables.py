import django_tables2 as tables 
from isah.models import Seal, SealType, SealSize
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django_tables2.utils import A




class sealTable(tables.Table):
    
    class Meta:
        model = Seal
        attrs = {'class':'bordered striped'}
        fields = ("size","seal_type", "serial_number", "created", "updated")



class sealTypeTable(tables.Table):

    def render_edit(self, record):
        return mark_safe('<a href='+reverse("isah:SealTypeEditForm", args=[record.pk])+'>Edit</a>')

    edit = tables.LinkColumn('isah:SealTypeEditForm', args=[A('pk')], empty_values=())

    def render_delete(self, record):
        return mark_safe('<a href='+reverse("isah:SealTypeDeleteForm", args=[record.pk])+'>Delete</a>')

    delete = tables.LinkColumn('isah:SealTypeDeleteForm', args=[A('pk')], empty_values=())

    class Meta:
        model = SealType 
        attrs = {'class':'bordered striped'}
        fields = ("name","description")


class sealSizeTable(tables.Table):

    def render_edit(self, record):
        return mark_safe('<a href='+reverse("isah:SealSizeEditForm", args=[record.pk])+'>Edit</a>')

    edit = tables.LinkColumn('isah:SealSizeEditForm', args=[A('pk')], empty_values=())

    def render_delete(self, record):
        return mark_safe('<a href='+reverse("isah:SealSizeDeleteForm", args=[record.pk])+'>Delete</a>')

    delete = tables.LinkColumn('isah:SealSizeDeleteForm', args=[A('pk')], empty_values=())

    class Meta:
        model = SealSize 
        attrs = {'class':'bordered striped'}
        fields = ("size", )

