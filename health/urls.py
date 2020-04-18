from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_index, name='health_index'),
    path('search/', views.search_health, name='search_health'),
    path('<int:pk>/', views.health_detail, name='health_detail'),
    
]