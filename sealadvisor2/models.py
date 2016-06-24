from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from seals.models import Company

# Create your models here.

class sealApplication(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=10)

	def __str__(self):
		return self.name


class supremeAftShaftInformation(models.Model):

	aft_shaft_size = models.IntegerField(verbose_name='Aft shaft diameter (mm)', blank=True, null=True)
	aft_pcd_liner = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Aft seal liner PCD [mm]')
	aft_pcd_flange = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Aft seal flange ring PCD [mm]')
	aft_centering_edge = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Aft seal flange ring centering edge [mm]')


class supremeFwdShaftInformation(models.Model):
	fwd_shaft_size = models.IntegerField(verbose_name='Forward shaft diameter (mm)', blank=True, null=True)
	fwd_pcd_liner = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='forward seal liner PCD [mm]')
	fwd_pcd_flange = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='forward seal flange PCD [mm]')
	fwd_centering_edge = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='forward seal centering edge [mm]')



class supremeAdvise(models.Model):

	# first ask for general information 

	company = models.ForeignKey(Company, verbose_name='Company (or leave blank)', null=True, blank=True)
	application = models.ForeignKey(sealApplication)

	CHOICES = (
		('fpp', 'Fixed pitch'),
		('cpp', 'Controllable pitch')
	)

	cpp_fpp = models.CharField(max_length=10,choices=CHOICES,verbose_name='Fixed or controllable pitch propellor')

	# in case that application is equal to 'sterntube', are both the forward and/or aft seal required?

	fwd_seal = models.BooleanField(default=False, verbose_name='Forward seal required?')
	aft_seal = models.BooleanField(default=False, verbose_name='Aft seal required?')


	rpm = models.IntegerField(verbose_name = 'Shaft rotational speed (RPM)')
	draught_shaft = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Shaft centerline draught (m)')


	fwd_seal_information = models.OneToOneField(supremeFwdShaftInformation, null=True, blank=True)
	aft_seal_information = models.OneToOneField(supremeAftShaftInformation, null=True, blank=True)

	def __str__(self):
		return str("Advise {id} - {application}").format(id=self.id, application=self.application)

