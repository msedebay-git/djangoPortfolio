from django.contrib import admin
from django.urls import path
from modelapp import views

urlpatterns = [
    path('stuall/', views.student_view),
    path('stu/', views.get_student)
]