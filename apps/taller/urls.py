from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculos/', views.vehiculos, name='vehiculos'),
    path('agregar-vehiculo/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('editar-vehiculo/', views.editar_vehiculo, name='editar_vehiculo'),
    path('eliminar-vehiculo/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('detalle-vehiculo/<int:vehiculo_id>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    path('nueva-visita/', views.nuevavisita, name='nueva_visita'),
    path('almacenar-visita/', views.almacenar_visita, name='almacenar_visita'),
]