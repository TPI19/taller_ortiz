from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    
    path('cliente', views.clientes, name='clientes'),

    #   -- Gestión de Vehículos --
    
    path('vehiculos/', views.vehiculos, name='vehiculos'),
    path('agregar-vehiculo/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('editar-vehiculo/', views.editar_vehiculo, name='editar_vehiculo'),
    path('eliminar-vehiculo/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('detalle-vehiculo/<int:vehiculo_id>/', views.detalle_vehiculo, name='detalle_vehiculo'),

    #   -- Gestión de Citas (Por parte del Cliente)  --

    # path('eliminar-visita/', views.eliminar_visita, name='eliminar_visita'),
    # path('nueva-visita/', views.nuevavisita, name='nueva_visita'),
    # path('almacenar-visita/', views.almacenar_visita, name='almacenar_visita'),
    # path('gestionar_visitas/', views.visita_list, name='gestionar_visitas'),

    # path('citas/', views.citas, name='citas'),

    #   -- Gestión de Visitas (Por parte del Admin)  --

    path('gestion-visitas-cliente/<int:cliente_id>', views.gestion_visitas_cliente, name='gestion_visitas_cliente'),
    path('registrar-visita/', views.registrar_visita, name='registrar_visita'),

    #   -- Gestión de Procesos (Por parte del Admin)  --

    path('gestion-procesos-visita/<int:visita_id>', views.gestion_procesos_visita, name='gestion_procesos_visita'),
    path('registrar-proceso/', views.registrar_proceso, name='registrar_proceso'),


     #   -- Gestión de Slots --

    path('editar-slot/', views.editar_slot, name='editar_slot'),
    path('edit-slot/', views.slot_edit, name='slot_edits'),
    
    
    path('eliminar-slot/', views.eliminar_slot, name='eliminar_slot'),
    
    
    path('especialidad/', views.especializaciones, name='especialidad'),
    path('agregar-especialidad/', views.almacenar_especialidad, name='agregar_especialidad'),
    # path('registro-especialidad/', views.registro_especialidad, name='registro_especialidad'),
    path('editar-especialidad/', views.editar_especialidad, name='editar_especialidad'),
    path('eliminar-especialidad/', views.eliminar_especialidad, name='eliminar_especialidad'),
    
    path('servicios/', views.servicios, name='servicios'),
    path('instalaciones/', views.instalaciones, name='instalaciones'),
    path('contactos/', views.contactos, name='contactos'),
    path('gestionar_slots/', views.slot_list, name='gestionar_slots'),
    path('almacenar-slots/', views.almacenar_slots, name='almacenar_slots'),
    
]