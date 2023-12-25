from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def add(request):
    try:
        num1 = float(request.POST.get('num1', 0))
        num2 = float(request.POST.get('num2', 0))
        result = num1 * num2
        return render(request, 'result.html', {'result': result})
    except (ValueError, TypeError):
        # Handle invalid input or conversion errors
        return HttpResponse("Invalid input. Please provide valid numbers.")

# def add(request):
#     a = request.GET['num1']
#     b = request.GET['num2']
#     ressult = a+b
#     return render(request, 'result.html', {'result':ressult})
