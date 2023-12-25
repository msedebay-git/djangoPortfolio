from django.urls import include, path
from myapp import views


urlpatterns = [
    path('v1', views.v1),
    path('v2', views.v2)
]

