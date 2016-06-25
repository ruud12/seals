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


class environmentalInformation(models.Model):
	eal = models.BooleanField(default=False, verbose_name='EAL oil used?')
	vgp = models.BooleanField(default=False, verbose_name= 'Compliance with VGP (American waters)')
	zero_leakage = models.BooleanField(default=False, verbose_name= 'Zero leakage (ventus/athmos)')

	CHOICES = (
		('ventus', 'Ventus'),
		('athmos', 'Athmos'),
	)

	zero_leakage_type = models.CharField(max_length=20, choices=CHOICES, verbose_name="Zero leakage system",blank=True)


class supremeAftShaftInformation(models.Model):

	aft_shaft_size = models.DecimalField(max_digits=5, decimal_places=1,verbose_name='Aft shaft diameter (mm)')
	aft_pcd_liner = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Aft seal liner PCD [mm]')
	aft_pcd_flange = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Aft seal flange ring PCD [mm]')
	aft_centering_edge = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Aft seal flange ring centering edge [mm]')


class supremeFwdShaftInformation(models.Model):
	fwd_shaft_size = models.DecimalField(max_digits=5, decimal_places=1,verbose_name='Forward shaft diameter (mm)')
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


	rpm = models.DecimalField(max_digits=4, decimal_places=0, verbose_name = 'Shaft rotational speed (RPM)')
	draught_shaft = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Shaft centerline draught (m)')


	fwd_shaft_information = models.OneToOneField(supremeFwdShaftInformation, null=True, blank=True, on_delete=models.CASCADE)
	aft_shaft_information = models.OneToOneField(supremeAftShaftInformation, null=True, blank=True, on_delete=models.CASCADE)

	environmental = models.OneToOneField(environmentalInformation, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return str("Advise {id} - {application}").format(id=self.id, application=self.application)

