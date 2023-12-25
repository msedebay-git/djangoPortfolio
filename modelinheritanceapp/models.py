from django.db import models


# Create your models here.
class CommonInfo(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    date = models.DateField()

    class Meta:
        abstract = True


class Trainer(CommonInfo):
    address = models.CharField(max_length=30)
    date = None


class Teacher(CommonInfo):
    salary = models.IntegerField()
    date = models.DateField()


class Bank(models.Model):
    bname = models.CharField(max_length=20)
    baddress = models.CharField(max_length=20)


class BankManager(Bank):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class University(models.Model):
    uname = models.CharField(max_length=20)
    ulocation = models.CharField(max_length=20)


class College(University):
    class Meta:
        proxy = True
        ordering = ['ulocation']
