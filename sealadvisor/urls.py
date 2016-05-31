from django.conf.urls import url
from sealadvisor import views
from sealadvisor.forms import AddAdvise1, AddAdvise2, AddAdvise3


app_name = 'sealadvisor'

advisor_forms = [AddAdvise1, AddAdvise2, AddAdvise3]

urlpatterns = [
	# url(r'^$', views.index, name='index'),
	url(r'^$', views.ContactWizard.as_view(advisor_forms, condition_dict={'1': views.sterntube_chosen})),
]