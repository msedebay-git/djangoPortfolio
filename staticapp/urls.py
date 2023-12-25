from django.urls import include, path
from staticapp import views

urlpatterns = [
    path('', views.my_view)
]
