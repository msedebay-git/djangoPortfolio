from django.contrib import admin
from django.urls import path
from modelapp3 import views

urlpatterns = [
    path('', views.emp_view),
]