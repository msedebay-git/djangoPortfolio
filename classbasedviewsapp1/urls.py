from django.urls import path
from classbasedviewsapp1 import views

urlpatterns = [
    path('cls/', views.ClsView.as_view()),
    path('cls1/', views.ClsView1.as_view()),
    path('fun/', views.fun_view),
    path('clsb/', views.clsBasedView.as_view()),
]
