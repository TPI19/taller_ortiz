from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Vehiculo, Visita, Cliente, Tecnico, Especializacion
from .models import User
from apps.users.views import registro_cliente
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import TecnicoForm

# Create your views here.
def index(request):
	contexto = {}	
	return render(request, 'index.html', contexto)

def vehiculos(request):

	cliente = Cliente.objects.get(user=request.user.id)
	
	vehiculos = Vehiculo.objects.filter(cliente=cliente)

	contexto = {
        'vehiculos': vehiculos,
    }
	
	return render(request, 'vehiculo/vehiculos.html', contexto)

def agregar_vehiculo(request):

	cliente = Cliente.objects.get(user = request.user.id)

	vehiculo = Vehiculo()
	vehiculo.cliente = cliente
	vehiculo.placa = request.POST['placa']
	vehiculo.tipo = request.POST['tipo']
	vehiculo.marca = request.POST['marca']
	vehiculo.modelo = request.POST['modelo']
	vehiculo.anio = int(request.POST['anio'])
	vehiculo.save()

	return redirect('vehiculos')

def editar_vehiculo(request):

	vehiculo = Vehiculo.objects.get(pk=request.POST['id_edit'])
	vehiculo.placa = request.POST['placa_edit']
	vehiculo.tipo = request.POST['tipo_edit']
	vehiculo.marca = request.POST['marca_edit']
	vehiculo.modelo = request.POST['modelo_edit']
	vehiculo.anio = int(request.POST['anio_edit'])
	vehiculo.save()

	return redirect('vehiculos')

def eliminar_vehiculo(request):

	Vehiculo.objects.filter(id=request.POST['id_delete']).delete()

	return redirect('vehiculos')

def detalle_vehiculo(request,vehiculo_id):

	try:

		vehiculo = Vehiculo.objects.get(pk=vehiculo_id)

	except Vehiculo.DoesNotExist:
		return render(request, 'base/not_found.html')

	return render(request, 'vehiculo/detalle.html', {'vehiculo': vehiculo})


def registro_tecnico(request):
	contexto={}
	return render(request, 'users/registro_empleado.html', contexto)


def almacenar_tecnico(request): 
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

	return redirect('empleados')

def eliminar_tecnico(request):
	Tecnico.objects.filter(id=request.POST['id_delete']).delete()
	return redirect('empleados')


def tecnicos(request):	
	tecnicos = Tecnico.objects.all()
	especializaciones = Especializacion.objects.all()
	contexto = {'tecnicos': tecnicos,'especializaciones': especializaciones,}
	return render(request, 'empleados/empleados.html', contexto)

def editar_tecnico(request):
	tecnico = Tecnico.objects.get(pk=request.POST['id_edit'])
	tecnico.user.first_name = request.POST['nombre_edit']
	tecnico.user.last_name = request.POST['apellido_edit']
	tecnico.user.email = request.POST['correo_edit']
	tecnico.especializacion.nombre = request.POST['especialidad_edit']
	tecnico.user.telefono = request.POST['telefono_edit']
	tecnico.user.direccion = request.POST['direccion_edit']
	tecnico.save()

	return redirect('empleados')

def clientes(request):	
	clientes = Cliente.objects.all()
	contexto = {'clientes': clientes,}
	return render(request, 'empleados/empleados.html', contexto)


# Muestra las diferentes especializaciones en el template
def especializaciones(request):	
	especializaciones = Especializacion.objects.all() # Obtiene todos los objetos de Especializacion
	contexto = {'especializaciones': especializaciones,}
	return render(request, 'especialidad/especialidad.html', contexto)


# Almacena las diferentes especialidades
def almacenar_especialidad(request):
	especialidad = Especializacion() # Se crea un objeto de tipo Especializacion
	especialidad.nombre = request.POST['nombre'] # Se asignan los valores a los atributos del objeto
	especialidad.descripcion = request.POST['descripcion']
	if Especializacion.objects.filter(nombre = request.POST['nombre']).exists():
		messages.error(request,'Ya existe esa especialidad')
	else:
		especialidad.save() # Se guardan los valores
	return redirect('especialidad')


# Edita las diferentes especialidades
def editar_especialidad(request):
	especialidad = Especializacion.objects.get(pk=request.POST['id_edit'])
	especialidad.nombre = request.POST['nombre_edit'] # Se asignan los valores a los atributos del objeto
	especialidad.descripcion = request.POST['descripcion_edit']
	if Especializacion.objects.filter(nombre = request.POST['nombre_edit']).exists():
		messages.error(request,'Ya existe esa especialidad')
	else:

		especialidad.save() # Se guardan los valores
	return redirect('especialidad')


def detalle_especialidad(request,especialidad_id):
	try:
		especialidad = Especializacion.objects.get(pk=especialidad_id)
	except Especializacion.DoesNotExist:
		return render(request, 'base/not_found.html')

	return render(request, 'especialidad/detalle.html', {'especialidad': especialidad})


def eliminar_especialidad(request):
	Especializacion.objects.filter(id=request.POST['id_delete']).delete()
	return redirect('especialidad')
