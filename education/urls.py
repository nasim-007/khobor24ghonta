from django.urls import path
from . import views

urlpatterns = [
    path('', views.education_index, name='education_index'),
    path('search/', views.search_education, name='search_education'),
    path('<int:pk>/', views.education_detail, name='education_detail'),
    
]