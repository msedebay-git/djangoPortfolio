from django.contrib import admin
from django.urls import path
from modelapp2 import views

urlpatterns = [
    path('', views.student_view),
]