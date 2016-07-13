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


class FwdSealOptions(models.Model):
	ocr = models.BooleanField(default=False, verbose_name='OCR ring')
	fkm = models.BooleanField(default=False, verbose_name='Use FKM lip-seals')


class AftSealOptions(models.Model):
	seaguard = models.BooleanField(default=False, verbose_name='Seaguard (backup oil repellant lip-seal)')

	CHOICES = (
		('shaft', 'Shaft centered'),
		('hub', 'Hub centered'),
	)

	linerCentering = models.CharField(max_length=20, choices=CHOICES, verbose_name='Liner centering')
	oring = models.BooleanField(default = False, verbose_name='O-ring between liner and shaft')
	anode = models.BooleanField(default = False, verbose_name='Kathodic protection')
	distanceRing = models.BooleanField(default = False, verbose_name='Distance ring')
	dirtBarrier = models.BooleanField(default = False, verbose_name='Dirt barrier')
	wireWinders = models.BooleanField(default = False, verbose_name='Wire winders')
	netCutters = models.BooleanField(default = False, verbose_name='Net cutters')
	hastelloy = models.BooleanField(default = False, verbose_name='Hastelloy springs')
	hml = models.BooleanField(default = False, verbose_name='Hard metal layer (HML)')
	air = models.BooleanField(default = False, verbose_name='Ventus/Athmos (depending on draught)')


class environmentalOptions(models.Model):
	vgp = models.BooleanField(default=False, verbose_name='Has to comply with VGP regulations')

	OIL_CHOICES = (
		('mineral', 'Mineral oil'),
		('eal', 'EAL oil (bio degradable oil)'),
	)

	oil = models.CharField(max_length=20, choices=OIL_CHOICES, verbose_name='What kind of oil is used')

	oilType = models.CharField(max_length=100, verbose_name='What type of oil is used', blank=True, null=True)

	air = models.BooleanField(default = False, verbose_name='Use an air type system (Ventus/Athmos) to comply with VGP and reduce the pressure on the lip seals (only aft seal)')






class supremeAdvise(models.Model):

	# first ask for general information 

	application = models.ForeignKey(sealApplication)

	CHOICES = (
		('fpp', 'Fixed pitch'),
		('cpp', 'Controllable pitch')
	)

	cpp_fpp = models.CharField(max_length=10,choices=CHOICES,verbose_name='Fixed or controllable pitch propellor', blank=True, null=True)

	pressure_oring = models.BooleanField(default=False, verbose_name='Pressure O-ring')

	# in case that application is equal to 'sterntube', are both the forward and/or aft seal required?

	fwd_seal = models.BooleanField(default=False, verbose_name='Forward seal.')
	aft_seal = models.BooleanField(default=False, verbose_name='Aft seal.')

	vgp = models.BooleanField(default=False, verbose_name='Has to comply with VGP regulations')

	aft_build_in_length = models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Aft seal build in length [mm]', blank=True, null=True)

	aftSize = models.DecimalField(max_digits=5, decimal_places=0,verbose_name='Aft shaft diameter (mm)', blank=True, null=True)
	fwdSize = models.DecimalField(max_digits=5, decimal_places=0,verbose_name='Forward shaft diameter (mm)', blank=True, null=True)

	rpm = models.DecimalField(max_digits=4, decimal_places=0, verbose_name = 'RPM')
	draught_shaft = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Draught to (aft) shaft centerline [m]')


	aft = models.ForeignKey(AftSealOptions, null=True, blank=True)
	fwd = models.ForeignKey(FwdSealOptions, null=True, blank=True)
	environment = models.ForeignKey(environmentalOptions, null=True, blank=True)


	typeApproval = models.ForeignKey(Class, verbose_name='Type approval required (specify which or leave blank)', blank=True, null=True)


	def __str__(self):
		return str("Advise {id} - {application}").format(id=self.id, application=self.application)

