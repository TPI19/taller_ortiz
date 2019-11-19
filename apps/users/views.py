from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import User
from django.core import mail

from apps.taller.models import Cliente,Visita

# Create your views here.

def registro_cliente(request):

	contexto={}

	return render(request, 'users/registro_cliente.html', contexto)

def almacenar_cliente(request):

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

	return redirect('/')


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



