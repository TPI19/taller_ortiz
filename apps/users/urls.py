from django.urls import path

from . import views

urlpatterns = [
	
	path('login/', views.login, name='login'),

	#URLs para gestión de Usuario Cliente

    path('registro-cliente/', views.registro_cliente, name='registro_cliente'),
    path('almacenar-cliente/', views.almacenar_cliente, name='almacenar_cliente'),

]