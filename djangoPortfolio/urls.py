"""
URL configuration for djangoPortfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.template.backends import django
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('myapp1/', include('myapp1.urls')),
    path('myapp2', include('myapp2.urls')),
    path('staticapp/', include('staticapp.urls')),
    path('dtlapp/', include('dtlapp.urls')),
    path('modelapp/', include('modelapp.urls')),
    path('modelapp1/', include('modelapp1.urls')),
    path('modelapp2/', include('modelapp2.urls')),
    path('modelapp3/', include('modelapp3.urls')),
    path('dynamicurlapp/', include('dynamicurlapp.urls')),
    path('cookieapp/', include('cookieapp.urls')),
    path('sessionapp/', include('sessionapp.urls')),
    path('sessionapp1/', include('sessionapp1.urls')),
    path('sessionapp2/', include('sessionapp2.urls')),
    path('cacheapp/', include('cacheapp.urls')),
    path('autheticationapp/', include('autheticationapp.urls')),
    path('classbasedviewsapp1/', include('classbasedviewsapp1.urls')),
    path('classbasedviewsapp2/', include('classbasedviewsapp2.urls')),
    path('classbasedviewsapp3/', include('classbasedviewsapp3.urls')),
    path('classbasedviewsapp4/', include('classbasedviewsapp4.urls')),
    path('classbasedviewsapp5/', include('classbasedviewsapp5.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('paginationapp/', include('paginationapp.urls')),
    path('', include('middlewareapp.urls')),
]

