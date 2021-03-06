"""lagersmit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from ajax_select import urls as ajax_select_urls


from tastypie.api import Api
from angular.api import JobResource


job_resource = JobResource()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sealadvisor2/', include('sealadvisor2.urls')),
    url(r'^erp/', include('erp.urls')),
    url(r'^ajax_select/', include(ajax_select_urls)),
    url(r'^isah/', include('isah.urls')),
    url(r'^servicerapportage/', include('servicerapportage.urls')),
    url(r'^api/', include(job_resource.urls)),
]
