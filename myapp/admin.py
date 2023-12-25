from django.contrib import admin
# from .models import Student
from myapp.models import Student


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'address', 'email', 'age']


admin.site.register(Student, StudentAdmin)
