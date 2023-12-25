from django import forms


class StudentForm(forms.Form):
    name = forms.CharField()
    address = forms.CharField()
    msg = forms.CharField(widget=forms.Textarea)
