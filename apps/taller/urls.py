from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculos/', views.vehiculos, name='vehiculos'),
    path('agregar-vehiculo/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('editar-vehiculo/', views.editar_vehiculo, name='editar_vehiculo'),
    path('editar-slot/', views.editar_slot, name='editar_slot'),
    path('edit-slot/', views.slot_edit, name='slot_edits'),
    path('eliminar-vehiculo/', views.eliminar_vehiculo, name='eliminar_vehiculo'),
    path('eliminar-visita/', views.eliminar_visita, name='eliminar_visita'),
    path('eliminar-slot/', views.eliminar_slot, name='eliminar_slot'),
    path('detalle-vehiculo/<int:vehiculo_id>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    path('nueva-visita/', views.nuevavisita, name='nueva_visita'),
    path('almacenar-visita/', views.almacenar_visita, name='almacenar_visita'),
    path('servicios/', views.servicios, name='servicios'),
    path('instalaciones/', views.instalaciones, name='instalaciones'),
    path('contactos/', views.contactos, name='contactos'),
    path('gestionar_slots/', views.slot_list, name='gestionar_slots'),
    path('almacenar-slots/', views.almacenar_slots, name='almacenar_slots'),
    path('gestionar_visitas/', views.visita_list, name='gestionar_visitas'),

]