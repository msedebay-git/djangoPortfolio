from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView, RedirectView


# Create your views here.
def fun_view(request, templatename):
    return render(request, templatename)


class ClsView(View):
    templatename = ""

    def get(self, request):
        context = {'message': 'hello hyderabad'}
        return render(request, self.templatename, context)


class MyTemplateView(TemplateView):
    template_name = "temp.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'moham'
        context['address'] = 'Columbia'
        context['age'] = 37
        return context


class FlipKartView(RedirectView):
    url = 'https://flipkart.com'
