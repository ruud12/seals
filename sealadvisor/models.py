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

	CHOICES = (
		('fpp', 'Fixed pitch'),
		('cpp', 'Controllable pitch')
	)

	cpp_fpp = models.CharField(max_length=10,choices=CHOICES,verbose_name='Fixed or controllable pitch propellor')
	shaft_size = models.IntegerField(verbose_name='Shaft diameter (mm)')
	rpm = models.IntegerField(verbose_name = 'Shaft rotational speed (RPM)')
	draught_shaft = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Shaft centerline draught (m)')
	eal = models.BooleanField(default=False, verbose_name='EAL oil used?')
	forwardseal = models.BooleanField(default=False, verbose_name='Forward seal needed')
	aftseal = models.BooleanField(default=False, verbose_name='Aft seal needed')

	draught_shaft_min = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Shaft centerline draught max (m)')
	draught_shaft_max = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Shaft centerline draught min (m)')


	CENTERING_CHOICES = (
		('hub', 'Hub'),
		('shaft', 'Shaft'),
	)

	YES_NO = (
		('yes', 'Yes'),
		('no', 'No'),
	)

	WIREWINDERS = (
		('clockwise', 'Clockwise'),
		('counterclockwise', 'Counterclockwise'),
		('two', 'Two of each on one seal'),
	)

	liner_centering = models.CharField(max_length=20,choices=CENTERING_CHOICES, default='')
	oring = models.CharField(max_length=10, choices=YES_NO, default='yes', verbose_name='O-ring between shaft & liner (O-ring commonly used for FPP)')
	sandy = models.CharField(max_length=10, choices=YES_NO, default='no', verbose_name='Will the seal be applied in a sandy/dirty environment?')

	ventus = models.BooleanField(default=False, verbose_name='Include SUPREME Ventus?')
	athmos = models.BooleanField(default=False, verbose_name='Include SUPREME Athmos?')
	anode = models.BooleanField(default=False, verbose_name='Protection against corrosion using cathodic protection?')

	wirewinder = models.BooleanField(default=False, verbose_name='Protection against wires (wire-winder)?')
	netcutters = models.CharField(max_length=30, choices=WIREWINDERS, default='')