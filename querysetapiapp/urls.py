from django.urls import path
from paginationapp import views

urlpatterns = [
    path('fun/', views.page_view),
    path('cls/', views.PageListView.as_view()),
    path('detail/<int:pk>', views.PageDetailView.as_view())

]
