from django.urls import path
from . import views

urlpatterns = [
    path('', views.bangladesh_index, name='bangladesh_index'),
    path('search/', views.search_bangladesh, name='search_bangladesh'),
    path('<int:pk>/', views.bangladesh_detail, name='bangladesh_detail'),
    
]