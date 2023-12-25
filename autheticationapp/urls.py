from django.contrib import admin
from django.urls import path
from autheticationapp import views

urlpatterns = [
    path('', views.sign_up, name='signup'),
    path('login/',views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('changepassword/', views.user_change_password,name='changepassword'),
    path('changepassword1/', views.user_change_password1,name='changepassword1'),
]

