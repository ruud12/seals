from django.contrib import admin

# Register your models here.
from seals.models import Company, Seal, Vessel, contactPerson, Action, ActionType, Report
from django.contrib.auth.models import User

admin.site.register(Company)
admin.site.register(Seal)
admin.site.register(Vessel)
admin.site.register(contactPerson)
admin.site.register(Action)
admin.site.register(ActionType)
admin.site.register(Report)
