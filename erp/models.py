from django.db import models
from django.utils import timezone
from model_utils import FieldTracker

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


class contactPerson(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	company = models.ForeignKey(Company)
	position = models.CharField(max_length=100)

	def __str__(self):
		return str("{first_name} {last_name} ({position})").format(first_name=self.first_name, last_name=self.last_name, position=self.position)	


class Vessel(models.Model):
	name = models.CharField(max_length=100)
	company = models.ForeignKey(Company)
	imo = models.CharField(max_length=10, verbose_name='IMO number')
	contacts = models.ManyToManyField(contactPerson, blank=True)

	def __str__(self):
		return self.name




class Seal(models.Model):
	x_number = models.CharField(max_length=20, verbose_name='X serial number')
	seal_type = models.CharField(max_length = 20, verbose_name='Seal type')
	size = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)
	vessel = models.ForeignKey(Vessel, blank=True, null=True)
	company = models.ForeignKey(Company)
	date_installed = models.DateField(verbose_name='Installed date')
	date_removed = models.DateField(verbose_name='Removed date', blank=True, null=True)


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
		return str("{number}x {part}").format(number=self.number,part=self.part, seal=self.seal)

class Mechanic(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)

	def __str__(self):
		return str("{first_name} {last_name}").format(first_name=self.first_name, last_name=self.last_name)

class serviceReport(models.Model):
	seal = models.ForeignKey(Seal)
	mechanics = models.ManyToManyField(Mechanic)
	date = models.DateField()
	superintendant = models.ForeignKey(contactPerson)


	parts_to_replace = models.ManyToManyField(sealComponent)


	def __str__(self):
		return self.seal.x_number + ' service report'


class confirmComponentChange(models.Model):
	seal = models.ForeignKey(Seal)
	report = models.ForeignKey(serviceReport)
	old_part = models.ForeignKey(Part, related_name='old_part')
	new_part = models.ForeignKey(Part, related_name='new_part')
	confirm = models.BooleanField(default=False)


