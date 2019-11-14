from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Vehiculo, Visita, Cliente

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


def nuevavisita(request):
	return render(request, 'nueva_visita.html')


def almacenar_visita(request):

	fecha1 = request.POST['fecha']
	caracter1 = request.POST['caracter']
	comentarios1 = request.POST['comentarios']
	slot_id1 = request.POST['slot']
	tecnico_id1 = request.POST['tecnico']
	vehiculo_id1 = request.POST['vehiculo']

	visita = Visita()
	
	visita.fecha = fecha1,
	visita.caracter = caracter1,
	visita.comentarios = comentarios1,
	visita.slot_id = slot_id1,
	visita.tecnico_id = tecnico_id1,
	visita.vehiculo_id = vehiculo_id1,

	visita.save()

	return redirect('/')



