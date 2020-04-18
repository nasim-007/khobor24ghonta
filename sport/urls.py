from django.urls import path
from . import views

urlpatterns = [
    path('', views.sport_index, name='sport_index'),
    path('search/', views.search_sport, name='search_sport'),
    path('<int:pk>/', views.sport_detail, name='sport_detail'),
    
]