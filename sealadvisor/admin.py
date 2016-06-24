from django.contrib import admin
from sealadvisor.models import Application, Advise, ApprovalType
from sealadvisor2.models import sealApplication, supremeAdvise

# Register your models here.

admin.site.register(sealApplication)
admin.site.register(Advise)
admin.site.register(ApprovalType)

admin.site.register(Application)
admin.site.register(supremeAdvise)

