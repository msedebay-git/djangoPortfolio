from django.urls import path
from dtlapp import views

urlpatterns = [
    path('emp/', views.emp_details),
    path('dt/',views.date_time),
    path('',views.my_view),
]