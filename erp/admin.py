from django.contrib import admin
from erp.models import Company, Seal, Part, partMaterial, partCategory, sealComponent, Vessel, sealComponentChange, serviceReport
# Register your models here.

admin.site.register(Company)
admin.site.register(Seal)
admin.site.register(Part)
admin.site.register(partMaterial)
admin.site.register(partCategory)
admin.site.register(sealComponent)
admin.site.register(Vessel)
admin.site.register(sealComponentChange)
admin.site.register(serviceReport)