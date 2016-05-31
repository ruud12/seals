from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms

# Create your models here.

class Application(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=10)

	def __str__(self):
		return self.name

class Advise(models.Model):
	application = models.ForeignKey(Application)
	shaft_size_aft = models.IntegerField(verbose_name='Shaft diameter aft')
	shaft_size_forward = models.IntegerField(verbose_name='Shaft diameter forward')
	rpm = models.IntegerField(verbose_name = 'Shaft rotational speed (RPM)')
	draught_shaft = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Shaft centerline draught')
	eal = models.BooleanField(default=False, verbose_name='EAL oil used')
	forwardseal = models.BooleanField(default=False, verbose_name='Forward seal needed')
	aftseal = models.BooleanField(default=False, verbose_name='Aft seal needed')


