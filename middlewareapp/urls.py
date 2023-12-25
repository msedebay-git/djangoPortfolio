from django.urls import path
from middlewareapp import views

urlpatterns = [
    path('', views.v1),

]
