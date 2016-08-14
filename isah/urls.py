from django.conf.urls import url
from isah import views
from isah.models import Seal, SealType, SealSize

app_name='isah'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^seals/$', views.sealOverview, name='sealOverview'),
	url(r'^seals/add/$', views.Create.as_view(model=Seal, fields=['seal_type', 'size'], template_name = "isah/simple_form.html", success_url='/isah/seals/', extra_context={'title':'Create new seal','submit':'Create seal'}), name="sealCreate"),
	url(r'^seals/sizes/$', views.SealSizeOverview, name='SealSizeOverview'),
	url(r'^seals/sizes/add/$', views.SealSizeCreate, name='SealSizeCreateForm'),
	url(r'^seals/sizes/(?P<pk>\d+)/edit/$', views.SealSizeEdit, name='SealSizeEditForm'),
	url(r'^seals/sizes/(?P<pk>\d+)/delete/$', views.Delete.as_view(model=SealSize, template_name='isah/delete.html', success_url='/isah/seals/sizes/',extra_context={'title':'Delete seal size', 'submit':'Delete', 'cancel':'SealSizeOverview'}), name='SealSizeDeleteForm'),
	url(r'^seals/types/$', views.SealTypeOverview, name='SealTypeOverview'),
	url(r'^seals/types/add/$', views.SealTypeCreate, name='SealTypeCreateForm'),
	url(r'^seals/types/(?P<pk>\d+)/edit/$', views.SealTypeEdit, name='SealTypeEditForm'),
	url(r'^seals/types/(?P<pk>\d+)/delete/$', views.Delete.as_view(model=SealType, template_name='isah/delete.html', success_url='/isah/seals/types/',extra_context={'title':'Delete seal type', 'submit':'Delete', 'cancel':'SealTypeOverview'}), name='SealTypeDeleteForm'),
]
