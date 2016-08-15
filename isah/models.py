from django.db import models
from sealadvisor2.models import AftSealOptions, FwdSealOptions
from address.models import AddressField

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



    
    def __str__(self):
        return self.name


class SealVessel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    company = models.ForeignKey(SealCompany, on_delete=models.CASCADE, verbose_name='Company')
    imo_number = models.CharField(max_length=10, verbose_name="IMO number")

    def __str__(self):
        return self.name


class SealType(models.Model):
    name = models.CharField(max_length=10, help_text="Type such as 'STA'")
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class SealSize(models.Model):
    size = models.IntegerField()
    
    def __str__(self):
        return str(self.size)
    


class Seal(models.Model):
    seal_type = models.ForeignKey(SealType, verbose_name='Type')
    size = models.ForeignKey(SealSize, verbose_name='Size')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Last updated')
    serial_number = models.CharField(max_length=15, verbose_name= 'Serial number')
    company = models.ForeignKey(SealCompany, on_delete=models.CASCADE, verbose_name='Company')
    vessel = models.ForeignKey(SealVessel, on_delete=models.CASCADE, verbose_name='Vessel', null=True, blank=True)


    
    
    
    
