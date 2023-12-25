from django.urls import path
from sessionapp2 import views

urlpatterns = [
    path('set/', views.set_session),
    path('get/', views.get_session),

]
