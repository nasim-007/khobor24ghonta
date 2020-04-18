from django.urls import path
from . import views

urlpatterns = [
    path('', views.international_index, name='international_index'),
    path('search/', views.search_international, name='search_international'),
    path('<int:pk>/', views.international_detail, name='international_detail'),
    
]