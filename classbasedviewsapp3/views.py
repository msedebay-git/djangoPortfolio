from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.list import ListView
from classbasedviewsapp3.models import Employee


# Create your views here.
class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    ordering = ['name']
    context_object_name = 'employees'


class EmployeeDetailsView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'
    pk_url_kwarg = 'empid'
