from django.conf.urls import url
from erp import views



app_name = 'erp'



urlpatterns = [
	url(r'^$', views.index, name='index'),
]