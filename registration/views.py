from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def profile(request):
    return render(request, 'registration/profile.html')


@staff_member_required()
def contact(request):
    return render(request, 'registration/contact.html')
