from django.urls import path
from . import views

urlpatterns = [
    path('', views.fashion_index, name='fashion_index'),
    path('search/', views.search_fashion, name='search_fashion'),
    path('<int:pk>/', views.fashion_detail, name='fashion_detail'),
    
]