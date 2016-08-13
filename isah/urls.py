from django.conf.urls import url
from isah import views
from isah.models import Seal, SealType, SealSize

app_name='isah'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^seals/$', views.sealOverview, name='sealOverview'),
	url(r'^seals/add/$', views.Create.as_view(model=Seal, fields=['seal_type', 'size'], template_name = "isah/simple_form.html", success_url='/isah/seals/', extra_context={'title':'Create new seal','submit':'Create seal'}), name="sealCreate"),
	url(r'^seals/type/add/$', views.Create.as_view(model=SealType, fields=['name', 'description'], template_name = "isah/simple_form.html", success_url='/isah/seals/', extra_context={'title':'Create new seal type', 'submit':'Create seal type'}), name="sealTypeCreate"),
	url(r'^seals/size/add/$', views.Create.as_view(model=SealSize, fields=['size'], template_name = "isah/simple_form.html", success_url='/isah/seals/', extra_context={'title':'Create new seal size', 'submit':'Create seal size'}), name="sealSizeCreate"),
]
