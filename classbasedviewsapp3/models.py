from django.db import models
from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    age = models.IntegerField()
    mail = models.EmailField(max_length=30)

    class Meta:
        db_table = 'myemp'
