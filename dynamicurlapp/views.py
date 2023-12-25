from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home1.html')


def emp_details(request, emp_id):
    if emp_id == 1:
        emp = {'id': emp_id, 'name': 'Moham', 'address': 'Columbia'}
    if emp_id == 2:
        emp = {'id': emp_id, 'name': 'John', 'address': 'Ellicot City'}
    if emp_id == 3:
        emp = {'id': emp_id, 'name': 'Peter', 'address': 'Baltimore'}
    if emp_id == 4:
        emp = {'id': emp_id, 'name': 'Robert', 'address': 'Laurel'}
    return render(request, 'employee.html', context=emp)
