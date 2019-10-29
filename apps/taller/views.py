from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Vehiculo, Visita

# Create your views here.
def index(request):

	contexto = {
    }
	
	return render(request, 'index.html', contexto)

def index_vehiculos(request):
	
	vehiculos = Vehiculo.objects.all()

	contexto = {
        'vehiculos': vehiculos,
    }
	
	return render(request, 'vehiculo/index.html', contexto)

def detalle_vehiculo(request,vehiculo_id):

	try:

		vehiculo = Vehiculo.objects.get(pk=vehiculo_id)

	except Vehiculo.DoesNotExist:
		return render(request, 'base/not_found.html')

	return render(request, 'vehiculo/detalle.html', {'vehiculo': vehiculo})

def edicion_vehiculo(request,vehiculo_id):

	try:

		vehiculo = Vehiculo.objects.get(pk=vehiculo_id)
		vehiculo.placa = request.POST['placa']
		vehiculo.tipo = request.POST['tipo']
		vehiculo.marca = request.POST['marca']
		vehiculo.modelo = request.POST['modelo']
		vehiculo.anio = int(request.POST['anio'])
		vehiculo.save()
		# selected_choice = vehiculo.anio_set.get(pk=request.POST['choice'])

	except Vehiculo.DoesNotExist:
		return render(request, 'base/not_found.html')

	return render(request, 'vehiculo/detalle.html', {'vehiculo': vehiculo})

