from django.urls import path
from . import views

urlpatterns = [
    path('', views.funny_index, name='funny_index'),
    path('search/', views.search_funny, name='search_funny'),
    path('<int:pk>/', views.funny_detail, name='funny_detail'),
    
]