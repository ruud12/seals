from django.conf.urls import url
from sealadvisor import views
from sealadvisor.forms import Advise0, Advise1, Advise2, Advise3, Advise4, Advise5, Advise6


app_name = 'sealadvisor'

advisor_forms = [Advise0, Advise1, Advise2, Advise3, Advise4,Advise5, Advise6]

urlpatterns = [
	# url(r'^$', views.index, name='index'),
	url(r'^$', views.index, name='index'),
	url(r'^supreme/$', views.ContactWizard.as_view(
		advisor_forms, 
		condition_dict={
			'2': views.sterntube_chosen, 
			'4': views.ventus,
			'5': views.athmos,
		}
	), name='supreme_advisor'),
]