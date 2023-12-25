from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from classbasedviewsapp5.forms import StudentForm
from django.views.generic.base import TemplateView

from classbasedviewsapp5.models import Student


# Create your views here.
class StudentFormView(FormView):
    template_name = 'student1.html'
    form_class = StudentForm
    success_url = '/success/'

    def form_valid(self, form):
        print(form.cleaned_data['name'])
        print(form.cleaned_data['address'])
        print(form.cleaned_data['msg'])
        return super().form_valid(form)


class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_form.html'
    fields = '__all__'
    success_url = '/success/'


class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'student_form.html'
    fields = '__all__'
    success_url = '/success/'


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    fields = '__all__'
    success_url = '/success/'


class SuccessTemplateView(TemplateView):
    template_name = 'success.html'


class NoDeleteTemplateView(TemplateView):
    template_name = 'nodelete.html'
