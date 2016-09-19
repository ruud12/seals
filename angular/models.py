from django.db import models


# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank = True)


