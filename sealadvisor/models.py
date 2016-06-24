from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
import datetime

# Create your models here.

class Application(models.Model):
	name = models.CharField(max_length=100)
	key = models.CharField(max_length=10)

	def __str__(self):
		return self.name



class ApprovalType(models.Model):
	key = models.CharField(max_length=10)

	className = models.CharField(max_length=100, verbose_name='Class')
	certificateNo = models.CharField(max_length=100, verbose_name='Certificate No.')
	issueDate = models.DateField(verbose_name='Date of issue', default=datetime.date.today())



	def __str__(self):
		return str("{className} - {certificateNo}").format(className=self.className, certificateNo=self.certificateNo)



class Advise(models.Model):




	application = models.ForeignKey(Application)

	CHOICES = (
		('fpp', 'Fixed pitch'),
		('cpp', 'Controllable pitch')
	)

	cpp_fpp = models.CharField(max_length=10,choices=CHOICES,verbose_name='Fixed or controllable pitch propellor')
	shaft_size = models.IntegerField(verbose_name='Shaft diameter aft seal (mm)')
	shaft_size_forward = models.IntegerField(verbose_name='Forward shaft diameter (mm)', blank=True, null=True)
	rpm = models.IntegerField(verbose_name = 'Shaft rotational speed (RPM)')
	draught_shaft = models.DecimalField(max_digits=5, decimal_places=1, verbose_name='Shaft centerline draught (m)')

	aft_pcd_liner = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Aft seal liner PCD [mm]')
	aft_pcd_flange = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Aft seal flange ring PCD [mm]')
	aft_pcd_centering = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Aft seal flange ring centering edge [mm]')

	forward_pcd_liner = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='forward seal liner PCD [mm]')
	forward_pcd_flange = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='forward seal flange PCD [mm]')
	forward_pcd_centering = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='forward seal centering edge [mm]')



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
		('no', 'No netcutter'),
		('clockwise', 'Clockwise'),
		('counterclockwise', 'Counterclockwise'),
		('two', 'Two of each on one seal'),
	)

	liner_centering = models.CharField(max_length=20,choices=CENTERING_CHOICES, default='')
	oring = models.CharField(max_length=10, choices=YES_NO, default='yes', verbose_name='O-ring between shaft & liner?')
	sandy = models.BooleanField(default=False, verbose_name='Will the seal be applied in a sandy/dirty environment?')

	ventus = models.BooleanField(default=False, verbose_name='Include SUPREME Ventus?')
	athmos = models.BooleanField(default=False, verbose_name='Include SUPREME Athmos?')
	anode = models.BooleanField(default=False, verbose_name='Protection against corrosion using cathodic protection?')

	wirewinder = models.BooleanField(default=False, verbose_name='Protection against wires (wire-winder)?')
	netcutters = models.BooleanField(default=False, verbose_name='Netcutters?')

	ocr = models.BooleanField(default=False, verbose_name='Oil collector ring')
	fkm_forward = models.BooleanField(default=False, verbose_name='FKM lip seals')
	hml_forward = models.BooleanField(default=False, verbose_name='HML wear resistant liner coating?')




	type_approval = models.ForeignKey(ApprovalType, verbose_name='Type approval required (specify which or leave blank)', blank=True, null=True)
	vgp = models.BooleanField(default=False, verbose_name= 'Compliance with VGP (American waters)')

	aft_liner_centering_edge = models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Aft seal liner centering edge [mm]')
	aft_built_in_length = models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Built in length [mm]')
	# Missing:
	# Centering edge liner flange [mm]
	# keramiek opties