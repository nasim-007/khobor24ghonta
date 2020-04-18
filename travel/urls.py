from django.urls import path
from . import views

urlpatterns = [
    path('', views.travel_index, name='travel_index'),
    path('search/', views.search_travel, name='search_travel'),
    path('<int:pk>/', views.travel_detail, name='travel_detail'),
    
]