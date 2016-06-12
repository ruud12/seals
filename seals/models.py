from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms

from django_countries.fields import CountryField
# Create your models here.





class Company(models.Model):
	name = models.CharField(max_length=100, verbose_name='Name')
	street = models.CharField(max_length=100, verbose_name ='Street name')
	streetNumber = models.IntegerField(verbose_name='Street number')
	city = models.CharField(max_length=100)
	country = CountryField()

	def __str__(self):
		return self.name

class contactPerson(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	user = models.OneToOneField(User,on_delete=models.CASCADE, blank=True, null=True)
	position = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=15)


	def __str__(self):
		return str('{first_name} {last_name}').format(first_name=self.first_name, last_name=self.last_name)


class Vessel(models.Model):
	name = models.CharField(max_length=100)
	imo_number = models.CharField(max_length=10)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	contact = models.ManyToManyField(contactPerson, verbose_name="Contact person(s)")



	def __str__(self):
		return self.name

class Seal(models.Model):
	created = models.DateTimeField(verbose_name='Created')
	serial_number = models.CharField(max_length=10, verbose_name='Serial number')
	size= models.IntegerField(verbose_name = 'Seal size')
	installedinvessel = models.ForeignKey(Vessel, verbose_name='Installed in vessel',on_delete=models.CASCADE)

	def __str__(self):
		return self.serial_number





class Report(models.Model):
	title = models.CharField(max_length=300,verbose_name='Title')
	remarks = models.CharField(max_length=1000,verbose_name='Remarks')
	relatedtoseal = models.ForeignKey(Seal, verbose_name='Related to seal')
	created = models.DateField(verbose_name='Created', default=timezone.now)

	def __str__(self):
		return self.title

class Action(models.Model):
	name = models.CharField(max_length=100)
	execute_date = models.DateField(default=timezone.now)
	remarks = models.CharField(max_length=1000, verbose_name='Remarks')
	relatedtoseal = models.ForeignKey(Seal, verbose_name='Related to seal')
	relatedtoreport = models.ForeignKey(Report, verbose_name='Related to report')


	def __str__(self):
		return self.name