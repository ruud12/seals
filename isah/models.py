from django.db import models

# Create your models here.


# overview of the model connections:
# 0: Seal (x-number)
# 1: Object (x-number): 
# 2: Vessel (IMO): 
# 3: Order (LS-number): 
# 4: Company


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
    seal_type = models.ForeignKey(SealType)
    size = models.ForeignKey(SealSize)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    serial_number = models.CharField(max_length=15)
    
    
    
    
    
