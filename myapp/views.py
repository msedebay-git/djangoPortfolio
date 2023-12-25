from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def v1(request):
    return HttpResponse("<h1>This is my first view</h1>")

def v2(request):
    return HttpResponse("<h1>This is my 2nd view</h1>")
