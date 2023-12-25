from django.urls import path
from classbasedviewsapp2 import views

urlpatterns = [
    path('fun1/', views.fun_view, {'templatename': 'fun1.html'}),
    path('fun2/', views.fun_view, {'templatename': 'fun2.html'}),
    path('cls1/', views.ClsView.as_view(templatename='cls1.html')),
    path('cls2/', views.ClsView.as_view(templatename='cls2.html')),
    path('temp/', views.MyTemplateView.as_view(extra_context={'mail': 'moham@gmail.com'})),
    path('flip/', views.FlipKartView.as_view()),
]
