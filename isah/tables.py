import django_tables2 as tables 
from isah.models import Seal, SealType, SealSize, SealCompany, SealVessel
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django_tables2.utils import A




class sealTable(tables.Table):

    def render_edit(self, record):
        return mark_safe('<a href='+reverse("isah:SealEditForm", args=[record.pk])+'>Edit</a>')

    edit = tables.LinkColumn('isah:SealEditForm', args=[A('pk')], empty_values=())

    def render_delete(self, record):
        return mark_safe('<a href='+reverse("isah:SealDeleteForm", args=[record.pk])+'>Delete</a>')


    serial_number = tables.LinkColumn('isah:SealDetail', args=[A('pk')])
    company = tables.LinkColumn('isah:SealCompanyDetail', args=[A('company.id')])

    delete = tables.LinkColumn('isah:SealDeleteForm', args=[A('pk')], empty_values=())
    
    class Meta:
        model = Seal
        attrs = {'class':'bordered striped white'}
        fields = ("serial_number", "seal_type", "size","company", "vessel", "created", "updated")



class sealTypeTable(tables.Table):

    def render_edit(self, record):
        return mark_safe('<a href='+reverse("isah:SealTypeEditForm", args=[record.pk])+'>Edit</a>')

    edit = tables.LinkColumn('isah:SealTypeEditForm', args=[A('pk')], empty_values=())

    def render_delete(self, record):
        return mark_safe('<a href='+reverse("isah:SealTypeDeleteForm", args=[record.pk])+'>Delete</a>')

    delete = tables.LinkColumn('isah:SealTypeDeleteForm', args=[A('pk')], empty_values=())

    class Meta:
        model = SealType 
        attrs = {'class':'bordered striped white'}
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
        attrs = {'class':'bordered striped white'}
        fields = ("size", )

class sealCompanyTable(tables.Table):

    def render_edit(self, record):
        return mark_safe('<a href='+reverse("isah:SealCompanyEditForm", args=[record.pk])+'>Edit</a>')

    edit = tables.LinkColumn('isah:SealCompanyEditForm', args=[A('pk')], empty_values=())

    def render_delete(self, record):
        return mark_safe('<a href='+reverse("isah:SealCompanyDeleteForm", args=[record.pk])+'>Delete</a>')

    delete = tables.LinkColumn('isah:SealCompanyDeleteForm', args=[A('pk')], empty_values=())

    name = tables.LinkColumn('isah:SealCompanyDetail', args=[A('pk')])

    class Meta:
        model = SealCompany 
        attrs = {'class':'bordered striped white'}
        fields = ("name","city","province")



class sealVesselTable(tables.Table):

    def render_edit(self, record):
        return mark_safe('<a href='+reverse("isah:SealVesselEditForm", args=[record.pk])+'>Edit</a>')

    edit = tables.LinkColumn('isah:SealVesselEditForm', args=[A('pk')], empty_values=())

    def render_delete(self, record):
        return mark_safe('<a href='+reverse("isah:SealVesselDeleteForm", args=[record.pk])+'>Delete</a>')

    delete = tables.LinkColumn('isah:SealVesselDeleteForm', args=[A('pk')], empty_values=())

    company = tables.LinkColumn('isah:SealCompanyDetail', args=[A('company.id')])

    class Meta:
        model = SealVessel
        attrs = {'class':'bordered striped white'}
        fields = ("name",'company','imo_number')