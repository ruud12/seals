from django.conf.urls import url
from sealadvisor import views
from sealadvisor.forms import AddAdvise1, AddAdvise2, AddAdvise3, AddAdvise4, AddAdvise5, AddAdvise6


app_name = 'sealadvisor'

advisor_forms = [AddAdvise1, AddAdvise2, AddAdvise3, AddAdvise4, AddAdvise5, AddAdvise6]

urlpatterns = [
	# url(r'^$', views.index, name='index'),
	url(r'^$', views.ContactWizard.as_view(
		advisor_forms, 
		condition_dict={

			'1': views.sterntube_chosen, 
			'3': views.ventus,
			'4': views.athmos,
		}
	)),
]