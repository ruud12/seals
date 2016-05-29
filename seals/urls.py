from django.conf.urls import url
from seals import views

app_name = 'seals'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<primary_key>[0-9]+)/$', views.detail, name='detail'),
	url(r'^company/(?P<primary_key>[0-9]+)/$', views.company, name='company'),
	url(r'^company/(?P<company_id>[0-9]+)/(?P<vessel_id>[0-9]+)/$', views.vessel, name='vessel'),
]