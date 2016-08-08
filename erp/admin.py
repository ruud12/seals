from django.contrib import admin
from erp.models import Company, Seal, Part, partMaterial, partCategory, sealComponent, Vessel, serviceReport,confirmComponentChange, Reason
# Register your models here.

admin.site.register(Company)
admin.site.register(Seal)
admin.site.register(Part)
admin.site.register(partMaterial)
admin.site.register(partCategory)
admin.site.register(sealComponent)
admin.site.register(Vessel)
admin.site.register(serviceReport)
admin.site.register(confirmComponentChange)
admin.site.register(Reason)
