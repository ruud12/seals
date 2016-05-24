from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django_countries.fields import CountryField
# Create your models here.





class Company(models.Model):
	name = models.CharField(max_length=100, verbose_name='Name')
	street = models.CharField(max_length=100, verbose_name ='Street name')
	streetNumber = models.IntegerField(max_length=3, verbose_name='Street number')
	city = models.CharField(max_length=100)
	country = CountryField()

	def __str__(self):
		return self.name

class contactPerson(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	position = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=15)


	def __str__(self):
		return self.user.first_name + self.user.last_name or self.user.username


class Vessel(models.Model):
	name = models.CharField(max_length=100)
	imo_number = models.CharField(max_length=10)
	contactPerson = models.ForeignKey(contactPerson, on_delete=models.CASCADE, related_name='vessel_contactperson')
	company = models.ForeignKey(Company, on_delete=models.CASCADE)



	def __str__(self):
		return self.name

class Seal(models.Model):
	serial_number = models.CharField(max_length=10)
	size= models.IntegerField(verbose_name = 'Seal size')
	installedInVessel = models.ForeignKey(Vessel, verbose_name='Installed in vessel',on_delete=models.CASCADE)

	def __str__(self):
		return self.serial_number