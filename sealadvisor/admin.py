from django.contrib import admin
from sealadvisor.models import Application, Advise, ApprovalType

# Register your models here.

admin.site.register(Application)
admin.site.register(Advise)
admin.site.register(ApprovalType)

