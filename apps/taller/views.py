from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Vehiculo, Visita, Cliente, Tecnico, Especializacion, Slot, User
from apps.users.views import registro_cliente
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.
def index(request):
	contexto = {}	
	return render(request, 'index.html', contexto)


#	-- GESTIÓN DE VEHICULOS POR CLIENTE --

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


#	-- GESTIÓN DE USUARIOS --

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

def slot_list(request):
	slot = Slot.objects.all()
	contexto = {'slots' : slot, }
	#return render (request,'gestionar_visitas.html', contexto)
	return render (request,'gestionar_slots.html', contexto)

def slot_edit(request):
	sloted = Slot.objects.get(pk=request.POST['id_edit'])
	contexto = {'sloted' : sloted, }
	#return render (request,'gestionar_visitas.html', contexto)
	return render (request,'gestionar_slots.html', contexto)


def visita_list(request):
	visita1 = Visita.objects.all()
	slot = Slot.objects.all()
	tecnico = Tecnico.objects.all()
	contexto = {'visitas' : visita1, 'slots' : slot, 'tecnicos' : tecnico}
	#tecnico = Tecnico.objects.filter(username = request.user.id)
	#visita = Visita.objects.all()
	#contexto = {'visitas' : visita, }
	return render (request,'gestionar_visitas.html', contexto)

def almacenar_visita(request):

	fecha1 = request.POST['fecha_visita']
	caracter1 = request.POST['caracter_visita']
	comentarios1 = request.POST['comentarios_visita']
	slot_id1 = request.POST['id_slot_visita']
	tecnico_id1 = request.POST['id_tecnico_visita']
	vehiculo_id1 = request.POST['id_vehiculo_visita']	


	visita = Visita()
	
	visita.fecha = fecha1
	visita.caracter = caracter1
	visita.comentarios = comentarios1
	visita.slot_id = slot_id1
	visita.tecnico_id = tecnico_id1
	visita.vehiculo_id = vehiculo_id1

	#visita.fecha = "2019-03-03"
	#visita.caracter = "hola"
	#visita.comentarios = "Esta es una prueba para ver como meter esta onda"
	#visita.slot_id = "58"
	#visita.tecnico_id = "1"
	#visita.vehiculo_id = "1"

	visita.save()

	return redirect('/')

def eliminar_visita(request):

	Visita.objects.filter(id=request.POST['id_delete']).delete()

	return redirect('gestionar_visitas')


def editar_slot(request):

	slot = Slot.objects.get(pk=request.POST['id_edit'])
	disponible1 = request.POST['disponible_edit']
	reservacion1 = request.POST['reservacion_edit']
	
	if disponible1 == "Disponible":
		variable = True
	else:
		variable = False

	if reservacion1 == "Reservado":
		variable2 = True
	else:
		variable2 = False

	slot.disponible = variable
	slot.reservacion = variable2

	slot.save()

	return redirect('gestionar_slots')


def eliminar_slot(request):

	Slot.objects.filter(id=request.POST['id_delete']).delete()

	return redirect('gestionar_slots')


def nuevavisita(request):
	slot1 = Slot.objects.all()
	contexto = {'slots' : slot1, }
	return render(request, 'nueva_visita.html', contexto)


def servicios(request):
	return render(request, 'servicios.html')


def instalaciones(request):
	return render(request, 'instalaciones.html')


def contactos(request):
	return render(request, 'contactos.html')

#def gestionar_slots(request):
#	contexto = {}	
#	return render(request, 'gestionar_slots.html', contexto)


def almacenar_slots(request):
	disponible1 = request.POST['Disponible']
	reservacion1 = request.POST['Reservacion']
	if disponible1 == "Disponible":
		variable = True
	else:
		variable = False

	if reservacion1 == "Reservado":
		variable2 = True
	else:
		variable2 = False
	slot = Slot()	
	slot.disponible = variable
	slot.reservacion = variable2
	slot.save()
	return redirect('gestionar_slots')