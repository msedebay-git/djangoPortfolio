from django.shortcuts import render, HttpResponse
from datetime import *


# Create your views here.
def set_cookie(request):
    response = HttpResponse("cookie has set")
    # response.set_cookie("name", 'moham',max_age=120)
    response.set_cookie('name', 'durgasoft', expires=datetime.utcnow() + timedelta(days=3))
    return response


def get_cookie(request):
    # nm = request.COOKIES
    nm = request.COOKIES.get('name', 'there is no cookie data')
    return HttpResponse('The cookie value is:' + nm)


def del_cookie(request):
    response = HttpResponse('Cookie has been deleted!')
    response.delete_cookie('name')
    return response


def count_view(request):
    if 'count' in request.COOKIES:
        newcount = int(request.COOKIES['count'])+1
    else:
        newcount = 1
    response = render(request, 'count.html', {'count': newcount})
    response.set_cookie('count',newcount)
    return response

