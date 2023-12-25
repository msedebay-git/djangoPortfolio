from django import forms


class StudentForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(required=False, max_length=20,disabled=True)
    address = forms.CharField(required=False,max_length=20,disabled=True)
    email = forms.CharField(required=False,max_length=30,disabled=True)
    age = forms.IntegerField(required=False,disabled=True)
