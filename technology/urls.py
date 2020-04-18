from django.urls import path
from . import views

urlpatterns = [
    path('', views.technology_index, name='technology_index'),
    path('search/', views.search_technology, name='search_technology'),
    path('<int:pk>/', views.technology_detail, name='technology_detail'),
    
]