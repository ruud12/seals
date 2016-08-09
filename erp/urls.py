from django.conf.urls import url
from erp import views



app_name = 'erp'



urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^allParts/$', views.viewAllParts, name='viewAllParts'),
	url(r'^allSeals/$', views.viewSeals, name='viewSeals'),
	url(r'^addPart/$', views.addPart, name='addPart'),
	url(r'^editPart/(?P<part_id>\d+)/$', views.editPart, name='editPart'),
	url(r'^addSeal/$', views.addSeal, name='addSeal'),
	url(r'^viewSeal/(?P<seal_id>\d+)/addComponent/$', views.addComponentToSeal, name='addComponentToSeal'),
	url(r'^viewSeal/(?P<seal_id>\d+)/addServiceReport/$', views.addServiceReport, name='addServiceReport'),
	url(r'^downloadServiceReport/(?P<report_id>\d+)/$', views.exportReportAsPDF, name='exportReportAsPDF'),
	url(r'^viewSeal/(?P<seal_id>\d+)/checkComponentChange/(?P<change_id>\d+)/$', views.checkComponentChange, name='checkComponentChange'),
	url(r'^viewSeal/(?P<seal_id>\d+)/$', views.viewSeal, name='viewSeal'),
	url(r'^addCompany/$', views.addCompany, name='addCompany'),
	url(r'^company/(?P<company_id>\d+)/addVessel/$', views.addVessel, name='addVessel'),
	url(r'^addVesselCompany/$', views.addVesselCompany, name='addVesselCompany'),
	url(r'^addMechanic/$', views.addMechanic, name='addMechanic'),
	url(r'^addCategory/$', views.addCategory, name='addCategory'),
	url(r'^addMaterial/$', views.addMaterial, name='addMaterial'),
	url(r'^addContactPerson/$', views.addContactPerson, name='addContactPerson'),
	url(r'^editCompany/(?P<company_id>\d+)/$', views.editCompany, name='editCompany'),
	url(r'^editVessel/(?P<vessel_id>\d+)/$', views.editVessel, name='editVessel'),
	url(r'^editMechanic/(?P<mechanic_id>\d+)/$', views.editMechanic, name='editMechanic'),
	url(r'^editSeal/(?P<seal_id>\d+)/$', views.editSeal, name='editSeal'),
	url(r'^editMaterial/(?P<material_id>\d+)/$', views.editMaterial, name='editMaterial'),
	url(r'^editCategory/(?P<category_id>\d+)/$', views.editCategory, name='editCategory'),
	url(r'^editContactPerson/(?P<contact_id>\d+)/$', views.editContactPerson, name='editContactPerson'),
]
