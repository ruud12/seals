from django.contrib import admin

from isah.models import SealCompany, SealSize, SealPart, Part, Seal

# Register your models here.

admin.site.register(SealCompany)
admin.site.register(SealSize)
admin.site.register(SealPart)
admin.site.register(Part)
admin.site.register(Seal)



