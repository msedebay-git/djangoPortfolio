from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(max_length=20)
    address = forms.CharField(max_length=30)
    age = forms.IntegerField()
