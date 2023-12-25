from django.urls import path
from classbasedviewsapp3 import views

urlpatterns = [
    path('emp/', views.EmployeeListView.as_view(template_name="employee_list.html")),
    path('emp/<int:empid>', views.EmployeeDetailsView.as_view(template_name="employee_detail.html")),

]
