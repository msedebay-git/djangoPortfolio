from django import forms
from modelapp3.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        # exclude = ['age']
        # error_messages = {'name':{'required':'name is mandatory'},'address':{'required':'address is must'}}
        # labels = {'name':'Enter Name:','address':'Enter address:','email':'Enter Address:','age':'Enter Age'}
