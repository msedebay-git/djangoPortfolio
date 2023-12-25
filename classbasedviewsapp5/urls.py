from django.urls import path
from classbasedviewsapp5 import views

urlpatterns = [
    path('student/', views.StudentFormView.as_view()),
    path('create/', views.StudentCreateView.as_view()),
    path('update/<int:pk>', views.StudentUpdateView.as_view()),
    path('delete/<int:pk>', views.StudentDeleteView.as_view()),
    path('success/', views.SuccessTemplateView.as_view()),
    path('nodelete/', views.NoDeleteTemplateView.as_view(), name='nodelete'),
]
