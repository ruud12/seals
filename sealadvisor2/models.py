from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class sealApplication(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=10)

	def __str__(self):
		return self.name


class Class(models.Model):
	key = models.CharField(max_length=10)

	className = models.CharField(max_length=100, verbose_name='Class')
	certificateNo = models.CharField(max_length=100, verbose_name='Certificate No.')

	def __str__(self):
		return str("{className} - {certificateNo}").format(className=self.className, certificateNo=self.certificateNo)


class AftSealOptions(models.Model):
	seaguard = models.BooleanField(default=False, verbose_name='Seaguard')

	CHOICES = (
		('shaft', 'Shaft centered'),
		('hub', 'Hub centered'),
	)

	linerCentering = models.CharField(max_length=20, choices=CHOICES, verbose_name='Liner centering')
	oring = models.BooleanField(default = True, verbose_name='O-ring between liner and shaft')



class supremeAdvise(models.Model):

	# first ask for general information 

	application = models.ForeignKey(sealApplication)

	CHOICES = (
		('fpp', 'Fixed pitch'),
		('cpp', 'Controllable pitch')
	)

	cpp_fpp = models.CharField(max_length=10,choices=CHOICES,verbose_name='Fixed or controllable pitch propellor', blank=True, null=True)

	# in case that application is equal to 'sterntube', are both the forward and/or aft seal required?

	fwd_seal = models.BooleanField(default=False, verbose_name='Forward seal.')
	aft_seal = models.BooleanField(default=False, verbose_name='Aft seal.')

	aftSize = models.DecimalField(max_digits=5, decimal_places=1,verbose_name='Aft shaft diameter (mm)', blank=True, null=True)
	fwdSize = models.DecimalField(max_digits=5, decimal_places=1,verbose_name='Forward shaft diameter (mm)', blank=True, null=True)

	rpm = models.DecimalField(max_digits=4, decimal_places=0, verbose_name = 'Nominal shaft revolutions per minute [RPM]')
	draught_shaft = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Shaft draught (aft) [m]')





	typeApproval = models.ForeignKey(Class, verbose_name='Type approval required (specify which or leave blank)', blank=True, null=True)


	def __str__(self):
		return str("Advise {id} - {application}").format(id=self.id, application=self.application)

