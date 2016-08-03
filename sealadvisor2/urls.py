from django.conf.urls import url
from sealadvisor2 import views
from erp.models import Company
from ajax_select import urls as ajax_select_urls


app_name = 'sealadvisor2'



urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^supreme/$', views.supreme, name='supreme'),
	url(r'^supreme/chooseSalesType/$', views.salesType, name='supremeSalesType'),
	url(r'^supreme/(?P<supreme_id>\d+)/edit/$', views.supremeEdit, name='supremeEdit'),
	url(r'^supreme/(?P<supreme_id>\d+)/aft/$', views.supremeAft, name='supremeAft'),
	url(r'^supreme/(?P<supreme_id>\d+)/fwd/$', views.supremeFwd, name='supremeFwd'),
	url(r'^supreme/(?P<supreme_id>\d+)/aft/(?P<aft_id>\d+)/edit$', views.supremeAftEdit, name='supremeAftEdit'),
	url(r'^supreme/(?P<supreme_id>\d+)/fwd/(?P<fwd_id>\d+)/edit$', views.supremeFwdEdit, name='supremeFwdEdit'),
	url(r'^supreme/(?P<supreme_id>\d+)/environment/$', views.supremeEnvironment, name='supremeEnvironment'),
	url(r'^supreme/(?P<supreme_id>\d+)/environment/(?P<env_id>\d+)/edit$', views.supremeEnvironmentEdit, name='supremeEnvironmentEdit'),
	url(r'^supreme/(?P<supreme_id>\d+)/overview/$', views.supremeOverview, name='supremeOverview'),
	url(r'^addcompany/$', views.CompanyCreate.as_view(), name="createCompany"),
	url(r'^updatecompany/(?P<pk>\d+)$', views.CompanyUpdate.as_view(success_url='/sealadvisor2/'), name="updateCompany"),
	url(r'^deletecompany/(?P<pk>\d+)$', views.CompanyDelete.as_view(success_url='/sealadvisor2/'), name="deleteCompany"),
	url(r'^deleteadvise/(?P<pk>\d+)$', views.AdviseDelete.as_view(success_url='/sealadvisor2/advises/'), name="deleteAdvise"),
	url(r'^companies/$', views.Companies, name='companies'),
	url(r'^advises/$', views.SupremeAdvises, name='advises'),
	url(r'^addtypeapproval/$', views.TypeApprovalCreate.as_view(success_url='/sealadvisor2/typeapprovals/'), name="createTypeApproval"),
	url(r'^updatetypeapproval/(?P<pk>\d+)$', views.TypeApprovalUpdate.as_view(success_url='/sealadvisor2/typeapprovals/'), name="updateTypeApproval"),
	url(r'^deletetypeapproval/(?P<pk>\d+)$', views.TypeApprovalDelete.as_view(success_url='/sealadvisor2/typeapprovals/'), name="deleteTypeApproval"),
	url(r'^typeapprovals/$', views.TypeApprovalOverview, name='typeApprovalOverview'),
	url(r'^addclass/$', views.ClassCreate.as_view(success_url='/sealadvisor2/class/'), name="createClass"),
	url(r'^updateclass/(?P<pk>\d+)$', views.ClassUpdate.as_view(success_url='/sealadvisor2/class/'), name="updateClass"),
	url(r'^deleteclass/(?P<pk>\d+)$', views.ClassDelete.as_view(success_url='/sealadvisor2/class/'), name="deleteClass"),
	url(r'^class/$', views.ClassOverview, name='classOverview'),
	#api urls
	url(r'^get_companies/$', views.get_companies, name='get_companies'),
	url(r'^companyEdit2/(?P<company_id>\d+)/$', views.CompanyDefaultsEdit, name='CompanyEdit2'),


]
