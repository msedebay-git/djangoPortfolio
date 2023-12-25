from django.contrib import admin
from .models import Teacher, Trainer, University, College
from .models import Bank, BankManager


# Register your models here.
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'address']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'age', 'salary']


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ['id', 'bname', 'baddress']


@admin.register(BankManager)
class BankManagerAdmin(admin.ModelAdmin):
    list_display = ['id', 'bname', 'baddress', 'name', 'age']


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ['id', 'uname', 'ulocation']


@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ['id', 'uname', 'ulocation']
