from django.shortcuts import render
from modelapp3.forms import EmployeeForm
from modelapp3.models import Employee
from django.contrib import messages


# Create your views here.
def emp_view(request):
    if request.method == 'POST':
        fm = EmployeeForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            ad = fm.cleaned_data['address']
            ml = fm.cleaned_data['email']
            ag = fm.cleaned_data['age']
            obj = Employee(name=nm,address=ad,email=ml,age=ag)
            obj.save()
            messages.add_message(request,messages.SUCCESS,'Record Inserted Successfully')
            # Create a new empty form to reset the form fields.
            fm = EmployeeForm()

        else:
            messages.info(request,'Please check the details')
    else:
        fm = EmployeeForm()
    return render(request, 'myemployee.html', {'form': fm})
