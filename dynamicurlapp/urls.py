from django.contrib import admin
from django.urls import path
from dynamicurlapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('emp/<int:emp_id>', views.emp_details, name='details'),
]

