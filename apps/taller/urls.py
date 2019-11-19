from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculos/', views.vehiculos, name='vehiculos'),
    path('cliente', views.clientes, name='clientes'),
    path('agregar-vehiculo/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('editar-vehiculo/', views.editar_vehiculo, name='editar_vehiculo'),
    path('eliminar-vehiculo/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('detalle-vehiculo/<int:vehiculo_id>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    path('empleados/', views.tecnicos, name='empleados'),
    path('almacenar-tecnico/', views.almacenar_tecnico, name='almacenar_tecnico'),
    path('editar-tecnico/', views.editar_tecnico, name='editar_tecnico'),
    path('eliminar-tecnico/', views.eliminar_tecnico, name='eliminar_tecnico'),
    path('registro-tecnico/', views.registro_tecnico, name='registro_tecnico'),
    path('especialidad/', views.especializaciones, name='especialidad'),
    path('agregar-especialidad/', views.almacenar_especialidad, name='agregar_especialidad'),
    # path('registro-especialidad/', views.registro_especialidad, name='registro_especialidad'),
    path('editar-especialidad/', views.editar_especialidad, name='editar_especialidad'),
    path('detalle-especialidad/<int:especialidad_id>/', views.detalle_especialidad, name='detalle_especialidad'),
    path('eliminar-especialidad/', views.eliminar_especialidad, name='eliminar_especialidad'),
]