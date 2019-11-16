from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Vehiculo, Visita, Cliente, Slot,Tecnico

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

def slot_list(request):
	slot = Slot.objects.all()
	contexto = {'slots' : slot, }
	#return render (request,'gestionar_visitas.html', contexto)
	return render (request,'gestionar_slots.html', contexto)

def visita_list(request):
<<<<<<< HEAD
	visita1 = Visita.objects.all()
	slot = Slot.objects.all()
	contexto = {'visitas' : visita1, 'slots' : slot, }
=======
	#tecnico = Tecnico.objects.filter(username = request.user.id)
	visita = Visita.objects.all()
	contexto = {'visitas' : visita, }
>>>>>>> 3114fee4a61990da5fae0868f01b7cee3c11f86a
	return render (request,'gestionar_visitas.html', contexto)

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






