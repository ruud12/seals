from django.conf.urls import url
from . import views

app_name = 'seals'
urlpatterns = [
	url(r'^$', views.index, name='index'),
]