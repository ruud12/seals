from django.contrib import admin

# Register your models here.
from seals.models import Company, Seal, Vessel, contactPerson, Report, Action, Sealstatus, Type
from django.contrib.auth.models import User

admin.site.register(Company)
admin.site.register(Seal)
admin.site.register(Vessel)
admin.site.register(contactPerson)
admin.site.register(Report)
admin.site.register(Action)
admin.site.register(Sealstatus)
admin.site.register(Type)