from django.shortcuts import render, redirect
from modelapp2.models import Student
from modelapp2.forms import StudentForm
from django.contrib import messages


# Create your views here.
def student_view(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            id = fm.cleaned_data['id']
            nm = fm.cleaned_data['name']
            ad = fm.cleaned_data['address']
            ml = fm.cleaned_data['email']
            ag = fm.cleaned_data['age']
            # for insert
            # s = Student(name=nm, address=ad, email=ml,age=ag)
            # s.save()

            # for update
            # s = Student(id=1, name=nm, address=ad, email=ml, age=ag)
            # s.save()

            # for delete
            s = Student(id=id)
            s.delete()

            messages.add_message(request, messages.SUCCESS, 'Data deleted successfully!')
        else:
            messages.info(request, 'Please enter valid details!')
    else:
        fm = StudentForm()
    return render(request, 'student.html', {'form': fm})

# def student_view(request, student_id=None):
#     if request.method == 'POST':
#         # Handle form submission for both creating and updating a student
#         if student_id is None:
#             # Create a new student
#             form = StudentForm(request.POST)
#         else:
#             # Update an existing student
#             student = Student.objects.get(pk=student_id)
#             form = StudentForm(request.POST, instance=student)
#
#         if form.is_valid():
#             form.save()
#             return redirect('student_list')  # Redirect to the list view after a successful update or create
#
#     else:
#         # Display the form for creating or editing a student
#         if student_id is None:
#             # Create a new student
#             form = StudentForm()
#         else:
#             # Edit an existing student
#             student = Student.objects.get(pk=student_id)
#             form = StudentForm(instance=student)
#
#     # List of all students
#     students = Student.objects.all()
#
#     return render(request, 'student.html', {'form': form, 'students': students})
#
#
# def delete_student(request, student_id):
#     if request.method == 'POST':
#         student = Student.objects.get(pk=student_id)
#         student.delete()
#         return redirect('student_list')
#     return render(request, 'confirm_delete.html', {'student_id': student_id})
