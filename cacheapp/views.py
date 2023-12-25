from django.shortcuts import render
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(30)
def v1(request):
    return render(request, 'sample1.html')


def v2(request):
    return render(request, 'sample2.html')


def v3(request):
    return render(request, 'sample3.html')
