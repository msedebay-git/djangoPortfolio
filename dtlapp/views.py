from django.shortcuts import render

# Create your views here.
def emp_details(request):
    eid = 123
    ename = "Moham"
    eaddress = "Columbia"
    designation = "Manager"
    age = 35
    details = {'eid':eid,'ename':ename,'eaddress':eaddress,'designation':designation,'age':age}
    return render(request,'emp.html',context=details)

from datetime import *

def date_time(request):
    dt = datetime.now()
    return render(request, 'date.html',{'dt':dt})

def my_view(request):
    names = {'names':['Saidou','Momodu','Moussa','Johnson']}
    return render(request, 'details.html', context=names)
    # return render(request, 'details.html',{'name':'Mohammed Sedebay','age':37}) //if loop

