from django.urls import path
from cacheapp import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('v1', cache_page(30)(views.v1)),
    path('v2', cache_page(30)(views.v2)),
    path('v3', views.v3),

]
