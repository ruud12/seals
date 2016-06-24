from django.conf.urls import url
from sealadvisor2 import views



app_name = 'sealadvisor2'



urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^supreme/$', views.supreme, name='supreme'),
	url(r'^supreme/(?P<supreme_id>[0-9])/$', views.supremeDetail, name='supremeDetail'),
	url(r'^supreme/(?P<supreme_id>[0-9])/fwd_seal$', views.supremeFwd, name='supremeFwd'),
]