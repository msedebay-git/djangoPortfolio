from django.shortcuts import render, HttpResponse


# Create your views here.

def set_session(request):
    request.session['city'] = 'columbia'
    request.session.set_expiry(300)
    return render(request, 'set.html')


def get_session(request):
    # city = request.session['city']
    city = request.session.get('city', default='no session data')
    session_age = request.session.get_expiry_age()
    session_date = request.session.get_expiry_date()
    return render(request, 'get.html', {'city': city,'sessionage':session_age, 'sessiondate':session_date})


def del_session(request):
    request.session.clear_expired()
    request.session.flush()
    if 'city' in request.session:
        del request.session['city']
    return render(request, 'del.html')
