from django.conf.urls import url
from seals import views

app_name = 'seals'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^seal/(?P<primary_key>[0-9]+)/$', views.detail, name='detail'),
	url(r'^company/(?P<primary_key>[0-9]+)/$', views.company, name='company'),
	url(r'^vessel/(?P<vessel_id>[0-9]+)/$', views.vessel_detail, name='vessel_detail'),
	url(r'^add_action/(?P<seal_id>[0-9]+)/(?P<report_id>[0-9]+)/$', views.add_action, name='add_action'),
	url(r'^(?P<seal_id>[0-9]+)/add_report/$', views.add_report, name='add_report'),
]