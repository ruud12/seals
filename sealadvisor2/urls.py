from django.conf.urls import url
from sealadvisor2 import views



app_name = 'sealadvisor2'



urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^supreme/$', views.supreme, name='supreme'),
	url(r'^supreme/(?P<supreme_id>\d+)/edit/$', views.supremeEdit, name='supremeEdit'),
	url(r'^supreme/(?P<supreme_id>\d+)/aft/$', views.supremeAft, name='supremeAft'),
	url(r'^supreme/(?P<supreme_id>\d+)/fwd/$', views.supremeFwd, name='supremeFwd'),
	url(r'^supreme/(?P<supreme_id>\d+)/aft/(?P<aft_id>\d+)/edit$', views.supremeAftEdit, name='supremeAftEdit'),
	url(r'^supreme/(?P<supreme_id>\d+)/fwd/(?P<fwd_id>\d+)/edit$', views.supremeFwdEdit, name='supremeFwdEdit'),
	url(r'^supreme/(?P<supreme_id>\d+)/environment/$', views.supremeEnvironment, name='supremeEnvironment'),
	url(r'^supreme/(?P<supreme_id>\d+)/environment/(?P<env_id>\d+)/edit$', views.supremeEnvironmentEdit, name='supremeEnvironmentEdit'),
	url(r'^supreme/(?P<supreme_id>\d+)/overview/$', views.supremeOverview, name='supremeOverview'),

]