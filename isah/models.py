from django.db import models
from sealadvisor2.models import AftSealOptions, FwdSealOptions

# Create your models here.


# overview of the model connections:
# 0: Seal (x-number)
# 1: Object (x-number): 
# 2: Vessel (IMO): 
# 3: Order (LS-number): 
# 4: Company



# Create your models here.





class SealCompany(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")

    # preferences for a company regarding the seal advisor
    aft_preferences = models.ForeignKey(AftSealOptions, on_delete=models.CASCADE)
    fwd_preferences = models.ForeignKey(FwdSealOptions, on_delete=models.CASCADE)


    street_and_number = models.CharField(max_length=100, null=True, blank=True, verbose_name="Address")
    postal_code = models.CharField(max_length=12, null=True, blank=True, verbose_name="Postal Code")
    province = models.CharField(max_length=100, null=True, blank=True, verbose_name="Province")
    city = models.CharField(max_length=100, null=True, blank=True, verbose_name="City")



    
    def __str__(self):
        return self.name


class SealVessel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    company = models.ForeignKey(SealCompany, on_delete=models.CASCADE, verbose_name='Company')
    imo_number = models.CharField(max_length=10, verbose_name="IMO number")

    def __str__(self):
        return self.name


class ContactPerson(models.Model):
    company = models.ForeignKey(SealCompany, verbose_name='Company')
    first_name = models.CharField(max_length=100, verbose_name='First name')
    last_name = models.CharField(max_length=100, verbose_name='Last name')
    email = models.EmailField()
    position = models.CharField(max_length=100, verbose_name="Position")

    def __str__(self):
        return self.first_name + " " + self.last_name

class SealType(models.Model):
    name = models.CharField(max_length=10, help_text="Type such as 'STA'")
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class SealSize(models.Model):
    size = models.IntegerField()
    
    def __str__(self):
        return str(self.size)
    
class Part(models.Model):
    name = models.CharField(max_length=100, help_text="Part name")
    applicable_sizes = models.ManyToManyField(SealSize, verbose_name='Applicable sizes')

    def __str__(self):
        return self.name





class Seal(models.Model):
    seal_type = models.ForeignKey(SealType, verbose_name='Type')
    size = models.ForeignKey(SealSize, verbose_name='Size')

    CHOICES = (
        ('N/A', 'Not applicable'),
        ('PS', 'Port side'),
        ('SB', 'Starboard')
    )

    side = models.CharField(max_length=10, choices=CHOICES, verbose_name='Side', help_text='At which side is the seal installed or leave blank in case of a single propellor')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last updated')
    serial_number = models.CharField(max_length=15, verbose_name= 'Serial number')
    company = models.ForeignKey(SealCompany, on_delete=models.CASCADE, verbose_name='Company')
    vessel = models.ForeignKey(SealVessel, on_delete=models.CASCADE, verbose_name='Vessel', null=True, blank=True)

    # parts list

    def __str__(self):
        return self.serial_number


class SealPart(models.Model):
    number_of_parts = models.IntegerField(verbose_name = "Number of this part in the seal")
    part = models.ForeignKey(Part, verbose_name = 'Part')

    CHOICES = (
            ('as_installed', 'As installed'),
            ('as_maintained', 'As maintained'),
    )

    status = models.CharField(verbose_name='Status', choices=CHOICES, max_length=20)
    seal = models.ForeignKey(Seal, verbose_name='Related seal')

    def __str__(self):
        return str("{number}x {part}").format(number = self.number_of_parts, part = self.part)




    
    
    
class LS(models.Model):
    LS_number = models.CharField(max_length=10, verbose_name='LS number')
    description = models.CharField(max_length=1000, null=True, blank=True, verbose_name='Description')
    company = models.ForeignKey(SealCompany, verbose_name='Company')
    seals = models.ManyToManyField(Seal, verbose_name='Related seals', blank=True)

    def __str__(self):
        return self.LS_number


class ServiceReport(models.Model):
    ls = models.ForeignKey(LS, verbose_name='LS order no.')
    vessel = models.ForeignKey(SealVessel, verbose_name='Serviced vessel')
    superintendant = models.ForeignKey(ContactPerson, verbose_name='Contact person')
    date_from = models.DateField(verbose_name='Start date')
    date_to = models.DateField(verbose_name='End date')
    location = models.CharField(max_length=200, verbose_name='Location')
    remarks = models.CharField(max_length=2000, verbose_name='Remarks', blank=True, help_text='General (not related to a seal) remarks')
