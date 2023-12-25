from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from classbasedviewsapp1.forms import StudentForm


# Create your views here.
class ClsView(View):
    name = "durgasoftClass"

    def get(self, request):
        # return HttpResponse('<h1>This is my first class based view </h1>')
        return HttpResponse(self.name)


class ClsView1(View):
    # city = 'Columbia'
    def get(self, request):
        context = {'city': 'city'}
        return render(request, 'cls.html', context)


def fun_view(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            print(fm.cleaned_data['address'])
            print(fm.cleaned_data['age'])
            return HttpResponse('Form data is submitted')
    else:
        fm = StudentForm()
    return render(request, 'funbased.html', {'form': fm})


class clsBasedView(View):
    def get(self, request):
        fm = StudentForm()
        return render(request, 'clsbased.html', {'form': fm})

    def post(self, request):
        fm = StudentForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            print(fm.cleaned_data['address'])
            print((fm.cleaned_data['age']))
        return HttpResponse("Form is submitted")
