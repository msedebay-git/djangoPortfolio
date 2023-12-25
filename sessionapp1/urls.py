from django.urls import path
from sessionapp1 import views

urlpatterns = [
    path('set/', views.set_session),
    path('check/', views.check_session),
    path('del/', views.del_session),
    path('', views.page_count_view),
]
