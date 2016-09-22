from django.conf.urls import url
from servicerapportage import views

app_name='servicerapportage'

urlpatterns = [
	url(r'^$', views.LSautocomplete.as_view(), name='index'),
        url(r'^report/$', views.ServiceReport, name = 'ServiceReportForm'),
	]
