from django.shortcuts import render
from modelapp1.forms import StudentForm


# Create your views here.
def student_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print("student name:",form.cleaned_data['name'])
            print("student address:",form.cleaned_data['address'])
            print("student mail:", form.cleaned_data['email'])
            print("student age:", form.cleaned_data['age'])
            print("student password:", form.cleaned_data['password'])
            print("student retype password:", form.cleaned_data['retype_password'])
        else:
            print('Please enter valid details')
    else:
        form = StudentForm()

    # form.order_fields(field_order=['name','age','email','address'])
    return render(request, 'studentform.html', {'form': form})
