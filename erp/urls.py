from django.conf.urls import url
from erp import views



app_name = 'erp'



urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^addSeal/$', views.addSeal, name='addSeal'),
	url(r'^viewSeal/(?P<seal_id>\d+)/$', views.viewSeal, name='viewSeal'),
	url(r'^addCompany/$', views.addCompany, name='addCompany'),
	url(r'^editCompany/(?P<company_id>\d+)/$', views.editCompany, name='editCompany'),
	url(r'^editSeal/(?P<seal_id>\d+)/$', views.editSeal, name='editSeal'),
]