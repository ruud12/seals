from django.conf.urls import url
from isah import views
from isah.models import Seal, SealType, SealSize, SealCompany, SealVessel

app_name='isah'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^seals/$', views.sealOverview, name='SealOverview'),
	url(r'^seals/(?P<pk>\d+)/$', views.SealDetail, name='SealDetail'),
	url(r'^seals/add/$', views.SealCreate, name="SealCreateForm"),
	url(r'^seals/(?P<pk>\d+)/edit/$', views.SealEdit, name='SealEditForm'),
	url(r'^seals/(?P<pk>\d+)/delete/$', views.Delete.as_view(model=Seal, template_name='isah/delete.html', success_url='/isah/seals/',extra_context={'title':'Delete seal ', 'submit':'Delete', 'cancel':'SealOverview'}), name='SealDeleteForm'),
	url(r'^seals/sizes/$', views.SealSizeOverview, name='SealSizeOverview'),
	url(r'^seals/sizes/add/$', views.SealSizeCreate, name='SealSizeCreateForm'),
	url(r'^seals/sizes/(?P<pk>\d+)/edit/$', views.SealSizeEdit, name='SealSizeEditForm'),
	url(r'^seals/sizes/(?P<pk>\d+)/delete/$', views.Delete.as_view(model=SealSize, template_name='isah/delete.html', success_url='/isah/seals/sizes/',extra_context={'title':'Delete seal size', 'submit':'Delete', 'cancel':'SealSizeOverview'}), name='SealSizeDeleteForm'),
	url(r'^seals/types/$', views.SealTypeOverview, name='SealTypeOverview'),
	url(r'^seals/types/add/$', views.SealTypeCreate, name='SealTypeCreateForm'),
	url(r'^seals/types/(?P<pk>\d+)/edit/$', views.SealTypeEdit, name='SealTypeEditForm'),
	url(r'^seals/types/(?P<pk>\d+)/delete/$', views.Delete.as_view(model=SealType, template_name='isah/delete.html', success_url='/isah/seals/types/',extra_context={'title':'Delete seal type', 'submit':'Delete', 'cancel':'SealTypeOverview'}), name='SealTypeDeleteForm'),
	url(r'^companies/$', views.SealCompanyOverview, name='SealCompanyOverview'),
	url(r'^companies/(?P<pk>\d+)/$', views.SealCompanyDetail, name='SealCompanyDetail'),
	url(r'^companies/add/$', views.SealCompanyCreate, name='SealCompanyCreateForm'),
	url(r'^companies/(?P<pk>\d+)/edit/$', views.SealCompanyEdit, name='SealCompanyEditForm'),
	url(r'^companies/(?P<pk>\d+)/delete/$', views.Delete.as_view(model=SealCompany, template_name='isah/delete.html', success_url='/isah/companies/',extra_context={'title':'Delete company', 'submit':'Delete', 'cancel':'SealCompanyOverview'}), name='SealCompanyDeleteForm'),
	url(r'^vessels/$', views.SealVesselOverview, name='SealVesselOverview'),
	url(r'^vessels/add/$', views.SealVesselCreate, name='SealVesselCreateForm'),
	url(r'^vessels/(?P<pk>\d+)/edit/$', views.SealVesselEdit, name='SealVesselEditForm'),
	url(r'^vessels/(?P<pk>\d+)/delete/$', views.Delete.as_view(model=SealVessel, template_name='isah/delete.html', success_url='/isah/vessels/',extra_context={'title':'Delete vessel', 'submit':'Delete', 'cancel':'SealVesselOverview'}), name='SealVesselDeleteForm'),
]
