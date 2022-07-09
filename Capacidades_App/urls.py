from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('base', views.base, name='base'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('searchbar', views.searchbar, name='searchbar'),
    #path('upload',views.simple_upload, name='upload'),
    path('editar_Capacidad/<int:ID_SGI>', views.editarCapacidad, name='editar_Capacidad'),
    path('crear_Capacidad/',views.crearCapacidad,name='crear_Capacidad'),
    path('eliminar_Capacidad/<int:ID_SGI>', views.eliminarCapacidad, name='eliminar_Capacidad'),
    #path('upload/',, name='upload'),
    path('upload-csv/', views.profile_upload, name="profile_upload")
]
