from django.db import models
from django.utils import timezone

# Create your models here.


class Company(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Seal(models.Model):
	xNumber = models.CharField(max_length=20, verbose_name='X serial number')
	sealType = models.CharField(max_length = 20, verbose_name='Seal type')
	size = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)

	company = models.ForeignKey(Company)

