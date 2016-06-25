from django.contrib import admin
from sealadvisor2.models import supremeFwdShaftInformation, supremeAftShaftInformation, environmentalInformation
# Register your models here.

admin.site.register(supremeFwdShaftInformation)
admin.site.register(environmentalInformation)
