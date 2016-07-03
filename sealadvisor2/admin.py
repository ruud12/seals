from django.contrib import admin

from sealadvisor2.models import supremeAdvise,  environmentalOptions, AftSealOptions, sealApplication

# Register your models here.

admin.site.register(supremeAdvise)
admin.site.register(environmentalOptions)
admin.site.register(AftSealOptions)
admin.site.register(sealApplication)



