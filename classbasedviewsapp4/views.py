from django.shortcuts import render
from classbasedviewsapp4.models import Manager
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.
class ManagerDetailView(DetailView):
    model = Manager
    template_name = 'manager_detail.html'


class ManagerListView(ListView):
    model = Manager
    template_name = 'manager_list.html'


