from django.shortcuts import render
from django.http import HttpRequest
from modelapp.models import Student


# Create your views here.
def student_view(request):
    student_data = Student.objects.all()
    return render(request, 'studentdetails.html', {'student_data': student_data})


def get_student(request):
    stu = Student.objects.get(pk=3)
    return render(request, 'getstudent.html', {'stu': stu})
