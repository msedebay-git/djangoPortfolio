from django.contrib import admin
from modelapp3.models import Employee


# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'email', 'age']
