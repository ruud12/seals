from django.conf.urls import url
from sealadvisor import views
from sealadvisor.forms import Advise0, Advise1, Advise2, Advise3, Advise4, Advise5, Advise6, AftOptions, ForwardOptions, Other


app_name = 'sealadvisor'

advisor_forms = [Advise0, Advise1, Advise2, AftOptions, Advise3, ForwardOptions, Advise4,Advise5, Advise6, Other]

urlpatterns = [
	# url(r'^$', views.index, name='index'),
	url(r'^$', views.index, name='index'),
	url(r'^supreme/$', views.ContactWizard.as_view(
		advisor_forms, 
		condition_dict={
			'1': views.sterntube_chosen, 
			'2': views.aft,
			'3': views.aft,
			'4': views.forward,
			'5': views.forward,
			'7': views.ventus,
			'8': views.athmos,
		}
	), name='supreme_advisor'),
]