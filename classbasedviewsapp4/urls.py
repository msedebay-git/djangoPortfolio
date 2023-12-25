from django.urls import path
from classbasedviewsapp4 import views

urlpatterns = [
    path('manager/', views.ManagerListView.as_view(), name='managerlist'),
    path('manager/<int:pk>', views.ManagerDetailView.as_view(), name='managerdetails'),

]
