from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def set_session(request):
    request.session['message'] = 'hi, how are you?'
    return render(request, 'set2.html')


def get_session(request):
    if 'message' in request.session:
        message = request.session['message']
        request.session.modified = True
        return render(request, 'get2.html', {'message': message})
    else:
        return HttpResponse('session has expired....')
