from django.contrib import admin

from sealadvisor2.models import supremeAdvise,  environmentalOptions, AftSealOptions, sealApplication
from erp.models import Company, Seal, Part, partMaterial, partCategory
# Register your models here.

admin.site.register(supremeAdvise)
admin.site.register(environmentalOptions)
admin.site.register(AftSealOptions)
admin.site.register(sealApplication)

admin.site.register(Company)
admin.site.register(Seal)
admin.site.register(Part)
admin.site.register(partMaterial)
admin.site.register(partCategory)

