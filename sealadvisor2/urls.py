from django.conf.urls import url
from sealadvisor2 import views



app_name = 'sealadvisor2'



urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^supreme/$', views.supreme, name='supreme'),
	url(r'^supreme/(?P<supreme_id>[0-9])/fwd_seal/(?P<fwd_id>[0-9])/edit/', views.supremeFwdEdit, name='supremeFwdEdit'),
	url(r'^supreme/(?P<supreme_id>[0-9])/fwd_seal/', views.supremeFwd, name='supremeFwd'),
	url(r'^supreme/(?P<supreme_id>[0-9])/aft_seal/(?P<aft_id>[0-9])/edit/', views.supremeAftEdit, name='supremeAftEdit'),
	url(r'^supreme/(?P<supreme_id>[0-9])/aft_seal/', views.supremeAft, name='supremeAft'),
	url(r'^supreme/(?P<supreme_id>[0-9])/environmental/(?P<environmental_id>[0-9])/edit', views.environmentalEdit, name='environmentalEdit'),
	url(r'^supreme/(?P<supreme_id>[0-9])/environmental/', views.environmental, name='environmental'),
	url(r'^supreme/(?P<supreme_id>[0-9])/edit$', views.supremeEdit, name='supremeEdit'),
	url(r'^supreme/(?P<supreme_id>[0-9])/detail$', views.supremeDetail, name='supremeDetail'),
	#url(r'^supreme/(?P<supreme_id>[0-9])/$', views.supremeDetail, name='supremeDetail'),
]