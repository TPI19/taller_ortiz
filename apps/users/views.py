from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import User

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
	# cliente.first_name = nombre
	# cliente.last_name = apellido
	# cliente.username = usuario
	# cliente.email = correo
	# cliente.set_password(password)
	# cliente.telefono = telefono
	# cliente.direccion = direccion
	# cliente.rol = rol
	# cliente.is_active = activo
	# cliente.is_staff = staff
	if cliente:
		user.set_password(password)
		user.save()

	contexto={}

	return render(request, 'users/registro_cliente.html', contexto)

def login(request):

	if(request.method == 'POST'):

		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request,'invalidad credentials')
			return redirect('login')

	else:
		return render(request,'users/login.html')