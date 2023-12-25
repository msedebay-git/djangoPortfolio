from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def my_view(request):
    return render(request, 'static.html')
