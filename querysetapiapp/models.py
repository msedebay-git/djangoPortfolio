from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    eid = models.IntegerField(unique=True, null=False)
    eaddress = models.CharField(max_length=30)
    age = models.IntegerField()
    dob = models.DateField()
