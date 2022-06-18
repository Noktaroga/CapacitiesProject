from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('base', views.base, name='base'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('searchbar', views.searchbar, name='searchbar'),
]
