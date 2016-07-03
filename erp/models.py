from django.db import models
from django.utils import timezone

# Create your models here.


class Company(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class partCategory(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class partMaterial(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Part(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=1000, null=True, blank=True)
	category = models.ForeignKey(partCategory)
	material = models.ForeignKey(partMaterial)
	number = models.IntegerField()
	size = models.IntegerField()

	def __str__(self):
		return str("{name} {size} ({material})").format(name=self.name, size=self.size, material=self.material)


class Vessel(models.Model):
	name = models.CharField(max_length=100)
	company = models.ForeignKey(Company)

	def __str__(self):
		return self.name




class Seal(models.Model):
	x_number = models.CharField(max_length=20, verbose_name='X serial number')
	seal_type = models.CharField(max_length = 20, verbose_name='Seal type')
	size = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)
	vessel = models.ForeignKey(Vessel, blank=True, null=True)
	company = models.ForeignKey(Company)

	def __str__(self):
		return self.x_number


class sealComponent(models.Model):
	number = models.IntegerField()
	part = models.ForeignKey(Part)
	seal = models.ForeignKey(Seal)

	CHOICES = (
		('as-installed', 'As installed'),
		('replacement', 'Replacement part (due to maintainance)'),
	)


	replaced_by = models.ForeignKey('self', null=True, blank=True, verbose_name='Replaced by component')

	status = models.CharField(max_length=20, choices=CHOICES)

	def __str__(self):
		return str("{seal} - {number}x {part}").format(number=self.number,part=self.part, seal=self.seal)



class serviceReport(models.Model):
	seal = models.ForeignKey(Seal)
	name = models.CharField(max_length=100)

