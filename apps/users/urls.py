from django.urls import path

from . import views

urlpatterns = [
	
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),

	path('', views.gestion_usuarios, name='gestion_usuarios'),

	#	-- URLs Gestión de Clientes --
	path('gestion-clientes/', views.gestion_clientes, name='gestion_clientes'),
    path('registrar-cliente/', views.registrar_cliente, name='registrar_cliente'),
    path('editar-cliente/', views.editar_cliente, name='editar_cliente'),
    path('eliminar-cliente/', views.eliminar_cliente, name='eliminar_cliente'),

	#	-- URLs Gestión de Técnicos --
	path('gestion-tecnicos/', views.gestion_tecnicos, name='gestion_tecnicos'),
    path('registrar-tecnico/', views.registrar_tecnico, name='registrar_tecnico'),
    path('editar-tecnico/', views.editar_tecnico, name='editar_tecnico'),
    path('eliminar-tecnico/', views.eliminar_tecnico, name='eliminar_tecnico'),

	

	#URLs para gestión de Usuario Cliente

    path('registro-cliente/', views.registro_cliente, name='registro_cliente'),
    

]