from django.shortcuts import render, HttpResponse


# Create your views here.
def v1(request):
    # print("This is a view v1")
    # print(10/0)
    return HttpResponse("<h2>This is my view v1</h2>")
