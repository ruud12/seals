from django.conf.urls import url
from seals import views

app_name = 'seals'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^detail/(?P<primary_key>[0-9])$/', views.detail, name='detail'),
]