from django.urls import path
from sessionapp import views

urlpatterns = [
    path('set/', views.set_session),
    path('get/', views.get_session),
    path('del/', views.del_session),



]