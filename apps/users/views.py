from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import User
from django.core import mail

from apps.taller.models import *

# Create your views here.


def gestion_usuarios(request):
	contexto = {}
	return render(request, 'gestion_usuarios/index_usuarios.html', contexto)

#	-- Vistas para Gestión de Técnicos --

def gestion_tecnicos(request):
	tecnicos = Tecnico.objects.all()
	especializaciones = Especializacion.objects.all()
	contexto = {
				'tecnicos': tecnicos,
				'especializaciones': especializaciones,
				}

	return render(request, 'gestion_usuarios/gestion_tecnicos.html', contexto)

def registrar_tecnico(request): 

	# Captura los datos del formulario
	nombre = request.POST['nombre']
	apellido = request.POST['apellido']
	usuario = request.POST['usuario']
	correo = request.POST['correo']
	password = request.POST['password']
	password_2 = request.POST['password-2']
	telefono = request.POST['telefono']
	direccion = request.POST['direccion']
	activo = True
	staff = True
	rol = 1

	if User.objects.filter(username = usuario).exists():
		messages.error(request,'Ya existe ese usuario, por favor ingrese otro usuario')

	else:
		user, tecnico = User.objects.get_or_create(
			username = usuario,
			first_name = nombre,
			last_name = apellido,
			email = correo,
			password = password,
			telefono = telefono,
			direccion = direccion,
			rol = rol,
			is_active = activo,
			is_staff = staff,
		)

		if tecnico:
			user.set_password(password)
			user.save()
		
		opcion_seleccionada = request.POST['especialidad_id'] # Captura el id de la especialidad seleccionada
		tecnico_taller = Tecnico() # Crea una instancia de Tecnico
		especialidad = Especializacion() # Crea una instancia de Especialidad
		# Obtiene la instancia de Especializacion por medio del id de la opcion seleccionada
		especialidad = Especializacion.objects.get(pk = opcion_seleccionada)
		# Asigna a los atributos del tecnico los valores de usuario y especialidad
		tecnico_taller.user = user 
		tecnico_taller.especializacion = especialidad
		tecnico_taller.save() # Guarda al tecnico

	return redirect('gestion_tecnicos')

def editar_tecnico(request):

	tecnico = Tecnico.objects.get(pk=request.POST['id_edit'])

	tecnico.user.first_name = request.POST['nombre_edit']
	tecnico.user.last_name = request.POST['apellido_edit']
	tecnico.user.username = request.POST['usuario_edit']
	tecnico.user.email = request.POST['correo_edit']
	tecnico.especializacion = Especializacion.objects.get(pk=request.POST['especialidad_edit'])
	tecnico.user.telefono = request.POST['telefono_edit']
	tecnico.user.direccion = request.POST['direccion_edit']
	tecnico.user.save()
	tecnico.save()

	return redirect('gestion_tecnicos')

def eliminar_tecnico(request):

	Tecnico.objects.filter(id=request.POST['id_delete']).delete()
	User.objects.filter(pk=request.POST['user_delete']).delete()

	return redirect('gestion_tecnicos')

#	-- Vistas para Gestión de Clientes --

def gestion_clientes(request):	
	clientes = Cliente.objects.all()
	contexto = {'clientes': clientes,}
	return render(request, 'gestion_usuarios/gestion_clientes.html', contexto)

def registrar_cliente(request):

	nombre = request.POST['nombre']
	apellido = request.POST['apellido']
	usuario = request.POST['usuario']
	correo = request.POST['correo']
	password = request.POST['password']
	password_2 = request.POST['password-2']
	telefono = request.POST['telefono']
	direccion = request.POST['direccion']
	activo = True
	staff = True
	rol = 2

	user, cliente = User.objects.get_or_create(
		username = usuario,
		first_name = nombre,
		last_name = apellido,
		email = correo,
		password = password,
		telefono = telefono,
		direccion = direccion,
		rol = rol,
		is_active = activo,
		is_staff = staff
	)
	
	if cliente:
		user.set_password(password)
		user.save()

	cliente_taller = Cliente()

	cliente_taller.user = user

	cliente_taller.save()

	if request.user.is_authenticated:

		return redirect('gestion_clientes')

	else:
		
		return redirect('/')

def editar_cliente(request):

	cliente = Cliente.objects.get(pk=request.POST['id_edit'])

	cliente.user.first_name = request.POST['nombre_edit']
	cliente.user.last_name = request.POST['apellido_edit']
	cliente.user.username = request.POST['usuario_edit']
	cliente.user.email = request.POST['correo_edit']
	cliente.user.telefono = request.POST['telefono_edit']
	cliente.user.direccion = request.POST['direccion_edit']
	cliente.user.save()
	cliente.save()

	return redirect('gestion_clientes')

def eliminar_cliente(request):

	Cliente.objects.filter(id=request.POST['id_delete']).delete()
	User.objects.filter(pk=request.POST['user_delete']).delete()

	return redirect('gestion_clientes')

#	-- Vistas para Login y LogOut --

def login(request):

	if(request.method == 'POST'):

		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.error(request,'Credenciales inválidas')
			return redirect('/')

	else:
		return render(request,'users/login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')

def registro_cliente(request):	#Para desplegar Formulario en Login

	contexto={}

	return render(request, 'users/registro_cliente.html', contexto)