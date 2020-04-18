from django.urls import path
from . import views

urlpatterns = [
    path('', views.politics_index, name='politics_index'),
    path('search/', views.search_politics, name='search_politics'),
    path('<int:pk>/', views.politics_detail, name='politics_detail'),
    
]