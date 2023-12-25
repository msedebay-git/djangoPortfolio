from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def set_session(request):
    request.session.set_test_cookie()
    return render(request, 'set1.html')


def check_session(request):
    if request.session.test_cookie_worked():
        message = 'User browser is supporting cookies'
        # print('User browser is supporting cookies')
    else:
        message = 'User browser does not support cookies'
        # print('User browser does not support cookies')

    # Using HttpResponse to send the message back to the client
    return HttpResponse(message)


def del_session(request):
    request.session.delete_test_cookie()
    return render(request, 'del1.html')


def page_count_view(request):
    count = request.session.get('count', 0)
    newcount = count+1
    request.session['count'] = newcount
    return render(request,'pagecount.html',{'count':count})
