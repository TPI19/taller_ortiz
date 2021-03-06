from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Administrador, Vehiculo, Visita, Cliente, Tecnico, Especializacion, Slot, User, ProcesoVisita, Proceso, Pieza, ProcesoPieza, Expediente, Cita
from apps.users.views import registro_cliente
from django.contrib import messages
from django.urls import reverse_lazy
from datetime import date, datetime

# Create your views here.

def index(request):
	if(request.user.is_authenticated and request.user.rol == 0):
		administrador = Administrador.objects.get(user_id=request.user.id)
		contexto = {'administrador':administrador}
	elif(request.user.is_authenticated and request.user.rol == 1):
		tecnico = Tecnico.objects.get(user_id=request.user.id)
		contexto = {'tecnico':tecnico}
	elif(request.user.is_authenticated and request.user.rol == 2):
		cliente = Cliente.objects.get(user_id=request.user.id)
		contexto = {'cliente':cliente}
	else:
		contexto = {}
		
	return render(request, 'index.html', contexto)

#	-- GESTIÓN DE VEHICULOS --

def vehiculos(request):

	cliente = Cliente.objects.get(user=request.user.id)
	
	vehiculos = Vehiculo.objects.filter(cliente=cliente)

	contexto = {
		'cliente':cliente,
        'vehiculos': vehiculos,
    }
	
	return render(request, 'vehiculo/vehiculos.html', contexto)

def vehiculos_admin(request,cliente_id):

	cliente = Cliente.objects.get(pk=cliente_id)
	
	vehiculos = Vehiculo.objects.filter(cliente=cliente)

	contexto = {
		'cliente':cliente,
        'vehiculos': vehiculos,
    }
	
	return render(request, 'vehiculo/vehiculos.html', contexto)

def agregar_vehiculo(request):

	cliente = Cliente.objects.get(user = request.POST['usuario_id'])

	vehiculo = Vehiculo()
	vehiculo.cliente = cliente
	vehiculo.placa = request.POST['placa']
	vehiculo.tipo = request.POST['tipo']
	vehiculo.marca = request.POST['marca']
	vehiculo.modelo = request.POST['modelo']
	vehiculo.anio = int(request.POST['anio'])
	vehiculo.save()

	expediente = Expediente()
	expediente.vehiculo = vehiculo
	expediente.detalle_mecanico = ''
	expediente.detalle_pintura = ''
	expediente.detalle_electrico = ''
	expediente.detalle_suspension = ''
	expediente.detalle_direccion = ''
	expediente.save()

	if(request.user.rol == 0):
		return redirect('vehiculos_admin', cliente_id=request.POST['cliente_id'])
	elif(request.user.rol == 2):
		return redirect('vehiculos')

def editar_vehiculo(request):

	vehiculo = Vehiculo.objects.get(pk=request.POST['id_edit'])
	vehiculo.placa = request.POST['placa_edit']
	vehiculo.tipo = request.POST['tipo_edit']
	vehiculo.marca = request.POST['marca_edit']
	vehiculo.modelo = request.POST['modelo_edit']
	vehiculo.anio = int(request.POST['anio_edit'])
	vehiculo.save()

	if(request.user.rol == 0):
		return redirect('vehiculos_admin', cliente_id=request.POST['cliente_id'])
	elif(request.user.rol == 2):
		return redirect('vehiculos')

def eliminar_vehiculo(request):

	Vehiculo.objects.filter(id=request.POST['id_delete']).delete()

	if(request.user.rol == 0):
		return redirect('vehiculos_admin', cliente_id=request.POST['cliente_id'])
	elif(request.user.rol == 2):
		return redirect('vehiculos')

def expediente_vehiculo(request,vehiculo_id):

	vehiculo = Vehiculo.objects.get(pk=vehiculo_id)
	expediente = Expediente.objects.get(vehiculo_id=vehiculo_id)

	contexto = {
		'vehiculo':vehiculo,
		'expediente':expediente,
	}

	return render(request, 'vehiculo/expediente.html', contexto)

def actualizar_expediente(request):

	vehiculo = Vehiculo.objects.get(pk=request.POST['vehiculo_id'])

	ult_visita = datetime.strptime(request.POST['ult_visita'], '%d/%m/%Y %H:%M %p')
	ult_visita.strftime('%Y/%m/%d %H:%M %A')

	ult_aceite = datetime.strptime(request.POST['ult_aceite'], '%d/%m/%Y %H:%M %p')
	ult_aceite.strftime('%Y/%m/%d %H:%M %A')

	prox_aceite = datetime.strptime(request.POST['prox_aceite'], '%d/%m/%Y %H:%M %p')
	prox_aceite.strftime('%Y/%m/%d %H:%M %A')

	ult_frenos = datetime.strptime(request.POST['ult_frenos'], '%d/%m/%Y %H:%M %p')
	ult_frenos.strftime('%Y/%m/%d %H:%M %A')

	prox_frenos = datetime.strptime(request.POST['prox_frenos'], '%d/%m/%Y %H:%M %p')
	prox_frenos.strftime('%Y/%m/%d %H:%M %A')

	expediente = Expediente.objects.get(pk=request.POST['expediente_id'])

	expediente.kilometraje = (int)(request.POST['kilometraje'])
	expediente.transmision = (int)(request.POST['transmision'])
	expediente.ult_visita = ult_visita
	expediente.ult_aceite = ult_aceite
	expediente.prox_aceite = prox_aceite
	expediente.ult_frenos = ult_frenos
	expediente.prox_frenos = prox_frenos
	expediente.detalle_mecanico = request.POST['detalle_mecanico']
	expediente.detalle_pintura = request.POST['detalle_pintura']
	expediente.detalle_electrico = request.POST['detalle_electrico']
	expediente.detalle_suspension = request.POST['detalle_suspension']
	expediente.detalle_direccion = request.POST['detalle_direccion']

	expediente.save()

	contexto = {
		'vehiculo':vehiculo,
		'expediente':expediente,
	}

	return render(request, 'vehiculo/expediente.html', contexto)


def detalle_vehiculo(request,vehiculo_id):

	try:

		vehiculo = Vehiculo.objects.get(pk=vehiculo_id)

	except Vehiculo.DoesNotExist:
		return render(request, 'base/not_found.html')

	return render(request, 'vehiculo/detalle.html', {'vehiculo': vehiculo})

# --- GESTIÓN DE VISITAS ---

def gestion_visitas_cliente(request,cliente_id):

	cliente = Cliente.objects.get(pk=cliente_id)
	tecnicos = Tecnico.objects.all
	slots = Slot.objects.all	
	vehiculos = Vehiculo.objects.filter(cliente=cliente)

	visitas_vehiculos = []
	for vehiculo in vehiculos:
		visitas_vehiculos.extend(Visita.objects.filter(vehiculo_id=vehiculo.id))

	visitas_activas = Visita.objects.filter(finalizada=0)

	tecnicos_ocupados = []
	for visita_activa in visitas_activas:
		tecnicos_ocupados.append(visita_activa.tecnico)

	contexto = {
		'tecnicos':tecnicos,
		'cliente': cliente,
		'slots':slots,
		'vehiculos':vehiculos,
		'visitas_vehiculos':visitas_vehiculos,
		'tecnicos_ocupados':tecnicos_ocupados,
	}

	return render(request, 'visitas/visitas-cliente.html', contexto)

def registrar_visita(request):

	d = datetime.strptime(request.POST['fecha_visita'], '%d/%m/%Y %H:%M %p')
	d.strftime('%Y/%m/%d %H:%M')

	expediente = Expediente.objects.get(vehiculo_id=request.POST['vehiculo_visita'])
	expediente.ult_visita = d
	expediente.save()

	visita = Visita()
	visita.fecha = d
	visita.caracter = request.POST['caracter_visita']
	visita.comentarios = request.POST['comentario_visita']
	visita.finalizada = False
	visita.slot_id = request.POST['slot_visita']
	visita.tecnico_id = request.POST['tecnico_visita']
	visita.vehiculo_id = request.POST['vehiculo_visita']
	visita.save()

	Slot.objects.filter(pk=request.POST['slot_visita']).update(disponible=0)

	return redirect('gestion_visitas_cliente',cliente_id=request.POST['cliente_visita'])

def editar_visita(request):

	d = datetime.strptime(request.POST['fecha_visita_edit'], '%d/%m/%Y %H:%M %p')
	d.strftime('%Y/%m/%d %H:%M')

	expediente = Expediente.objects.get(vehiculo_id=request.POST['vehiculo_visita_edit'])
	expediente.ult_visita = d
	expediente.save()

	visita = Visita.objects.get(pk=request.POST['visita_vehiculo_edit'])

	Slot.objects.filter(pk=visita.slot_id).update(disponible=1)
	
	visita.fecha = d
	visita.caracter = request.POST['caracter_visita_edit']
	visita.comentarios = request.POST['comentario_visita_edit']
	visita.slot_id = request.POST['slot_visita_edit']
	visita.tecnico_id = request.POST['tecnico_visita_edit']
	visita.vehiculo_id = request.POST['vehiculo_visita_edit']
	visita.save()

	Slot.objects.filter(pk=visita.slot_id).update(disponible=0)

	return redirect('gestion_visitas_cliente',cliente_id=request.POST['cliente_visita_edit'])

def finalizar_visita(request):

	visita = Visita.objects.get(pk=request.POST['id_visita_fin'])

	slot = Slot.objects.get(pk=visita.slot.id)

	visita.finalizada = True
	slot.disponible = True

	visita.save()
	slot.save()

	if((int)(request.POST['visita_index'])==1):

		return redirect('gestion_visitas_cliente',cliente_id=request.POST['cliente_visita'])

	elif((int)(request.POST['visita_index'])==0):

		return redirect('gestion_procesos_visita',visita_id=request.POST['id_visita_fin'])

	else:

		return redirect('gestion_visitas')

def gestion_visitas(request):

	visitas_activas = Visita.objects.filter(finalizada=0)

	contexto = {
		'visitas_activas':visitas_activas,
	}

	return render(request, 'visitas/visitas.html', contexto)

# --- GESTIÓN DE PROCESOS ---

def gestion_procesos_visita(request,visita_id):

	visita = Visita.objects.get(pk=visita_id)
	procesos = Proceso.objects.all
	procesos_visita = ProcesoVisita.objects.filter(visita_id=visita_id)
	tecnicos = Tecnico.objects.all
	piezas = Pieza.objects.all
	procesos_piezas = ProcesoPieza.objects.all

	contexto = {

		'procesos_piezas':procesos_piezas,
		'piezas':piezas,
		'tecnicos':tecnicos,
		'visita': visita,
		'procesos_visita':procesos_visita,
		'procesos':procesos,
	}
	
	return render(request, 'procesos/index-procesos.html', contexto)

def registrar_proceso_visita(request):

	visita = Visita.objects.get(pk=request.POST['id_visita'])

	proceso_visita = ProcesoVisita()

	proceso_visita.visita = visita
	proceso_visita.detalle = request.POST['detalle_proceso']

	if((int)(request.POST['nuevo'])==0):

		proceso = Proceso.objects.get(pk=request.POST['proceso'])

		proceso_visita.proceso = proceso

	else:

		proceso = Proceso()
		proceso.nombre=request.POST['nombre_nuevo']
		proceso.caracter = request.POST['caracter_nuevo']
		proceso.descripcion = request.POST['descripcion_nuevo']
		proceso.save()

		proceso_visita.proceso = proceso

	proceso_visita.save()	

	contexto = {}
	
	return redirect('gestion_procesos_visita',visita_id=request.POST['id_visita'])

# --- GESTIÓN DE PIEZAS EN PROCESOS ---

def piezas_proceso(request,proceso_visita_id):
	
	proceso_visita = ProcesoVisita.objects.get(pk=proceso_visita_id)
	proceso_piezas = ProcesoPieza.objects.filter(proceso_visita_id=proceso_visita_id)
	piezas = Pieza.objects.all

	contexto = {

		'proceso_visita':proceso_visita,
		'proceso_piezas':proceso_piezas,
		'piezas':piezas,

	}

	return render(request, 'piezas/piezas_proceso.html', contexto)

def registrar_pieza_visita(request):
	
	proceso_pieza = ProcesoPieza()

	proceso_pieza.pieza = Pieza.objects.get(pk=(int)(request.POST['pieza']))
	proceso_pieza.proceso_visita = ProcesoVisita.objects.get(pk=(int)(request.POST['id_proceso']))
	proceso_pieza.cantidad = request.POST['cantidad']

	proceso_pieza.save()

	return redirect('piezas_proceso', proceso_visita_id=request.POST['id_proceso'])

#	-- GESTIÓN DE USUARIOS --

def clientes(request):	
	clientes = Cliente.objects.all()
	contexto = {'clientes': clientes,}
	return render(request, 'empleados/empleados.html', contexto)

# --- GESTIÓN DE ESPECIALIDADES ---

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
	especialidad.descripcion = request.POST['descripcion_edit'] # Se asignan los valores a los atributos del objeto
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

# --- GESTIÓN DE SLOTS ---

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

# --- INFORMATIVAS ---

def servicios(request):
	return render(request, 'servicios.html')

def instalaciones(request):
	return render(request, 'instalaciones.html')

def contactos(request):
	return render(request, 'contactos.html')

#def gestionar_slots(request):
#	contexto = {}	
#	return render(request, 'gestionar_slots.html', contexto)





#	-- GESTIÓN DE CITAS POR CLIENTE --
def citas(request):
	cliente = Cliente.objects.get(user=request.user.id)
	citas = Cita.objects.filter(cliente=cliente)
	contexto = {
        'citas': citas,
    }
	return render(request, 'citas/citas.html', contexto)

def citasA(request):
	citas = Cita.objects.filter()	
	contexto = {
        'citas': citas,
    }
	return render(request, 'citas/citasA.html', contexto)	


def agregar_cita(request):

	cliente = Cliente.objects.get(user = request.user.id)
	cita = Cita()
	cita.cliente = cliente
	cita.fecha_propuesta = request.POST['fecha']
	cita.caracter= request.POST['caracter']
	cita.estado= request.POST['estado']
	cita.mensaje= request.POST['mensaje']
	cita.save()
	return redirect('citas')

def editar_cita(request):
	cita = Cita.objects.get(pk=request.POST['id_edit'])
	cita.fecha_propuesta = request.POST['fecha_edit'] 
	cita.caracter= request.POST['caracter_edit'] 
	cita.estado= int(request.POST['estado_edit'])
	cita.mensaje= request.POST['mensaje_edit']
	cita.save()
	return redirect('citas')

def editar_citaA(request):
	cita = Cita.objects.get(pk=request.POST['id_edit'])
	
	cita.caracter= request.POST['caracter_edit'] 
	cita.estado= int(request.POST['estado_edit'])
	cita.mensaje= request.POST['mensaje_edit']
	cita.save()
	return redirect('citasA')




def eliminar_cita(request):
	Cita.objects.filter(id=request.POST['id_delete']).delete()
	return redirect('citas')

def detalle_cita(request,cita_id):
	try:
		cita = Cita.objects.get(pk=cita_id)
	except Cita.DoesNotExist:
		return render(request, 'base/not_found.html')
	return render(request, 'cita/detalle.html', {'cita': cita})

