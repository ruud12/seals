from django.conf.urls import url
from isah import views

app_name='isah'

urlpatterns = [
	url(r'^$', views.index, name='index'),
]