from django.core import validators
from django import forms


def start_with_s(value):
    if value[0] != 's':
        raise validators.ValidationError("name should starts with letter s")


class StudentForm(forms.Form):
    name = forms.CharField(max_length=10, label="Enter fullname:",validators=[start_with_s])
    address = forms.CharField(max_length=20, label='Enter address:', validators=[validators.MaxLengthValidator(10)])
    email = forms.EmailField(max_length=30, label='Enter email:')
    age = forms.IntegerField(label='Enter age:')
    password = forms.CharField(required=False)
    retype_password = forms.CharField(required=False)

    def clean(self):
        super().clean()
        pwd = self.cleaned_data['password']
        rpwd = self.cleaned_data['retype_password']
        if pwd != rpwd:
            raise forms.ValidationError("Password mismatch")

    # particular field validation
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if len(name) < 6:
    #         raise forms.ValidationError("name must be 6 or more characters")

    # msg = forms.CharField(widget=forms.Textarea, help_text="Only 150 characters")

# class StudentForm(forms.Form):
#     name = forms.CharField(
#         max_length=50,
#         label="Full Name",
#         widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
#     )
#     address = forms.CharField(
#         max_length=100,
#         label="Address",
#         widget=forms.TextInput(attrs={'placeholder': 'Enter your address'}),
#     )
#     email = forms.EmailField(
#         max_length=100,
#         label="Email",
#         widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
#     )
#     age = forms.IntegerField(
#         label="Age",
#         widget=forms.NumberInput(attrs={'placeholder': 'Enter your age'}),
#     )
#     password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
#         label="Password",
#     )
#     msg = forms.CharField(
#         widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your message'}),
#         label="Message",
#         help_text="Limited to 150 characters",
#         max_length=150,
#     )
