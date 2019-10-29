from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculos/', views.index_vehiculos, name='index_vehiculos'),
    path('detalle-vehiculo/<int:vehiculo_id>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    path('edicion-vehiculo/<int:vehiculo_id>/', views.edicion_vehiculo, name='edicion_vehiculo'),
]