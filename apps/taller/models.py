from django.db import models
from apps.users.models import User

# Create your models here.

class Administrador(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

class Especializacion(models.Model):

	nombre = models.CharField(max_length=100)
	descripcion = models.TextField()

class Tecnico(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	especializacion = models.ForeignKey(Especializacion, on_delete=models.CASCADE)

class Cliente(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

class Cita(models.Model):

	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	administrador = models.ForeignKey(Administrador, on_delete=models.CASCADE)
	fecha_propuesta = models.DateTimeField()
	caracter = models.CharField(max_length=100)
	estado = models.IntegerField()
	mensaje = models.TextField()

class Slot(models.Model):

	disponible = models.BooleanField(default=False)
	reservacion = models.BooleanField(default=False)

class Vehiculo(models.Model):

	placa = models.CharField(max_length=8)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=100)
	marca = models.CharField(max_length=100)
	modelo = models.CharField(max_length=100)
	anio = models.IntegerField()

	def __str__(self):
		vehiculo_string = "{0} / {1} - {2} / {3}"
		return vehiculo_string.format(self.placa, self.marca, self.modelo, str(self.anio))

class Visita(models.Model):

	vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
	tecnico = models.ForeignKey(Tecnico, on_delete=models.CASCADE)
	slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
	fecha = models.DateTimeField()
	caracter = models.CharField(max_length=100)
	comentarios = models.TextField()
	finalizada = models.BooleanField(default=False)

	def __str__(self):
		visita_string = "{0} / {1} - {2} / {3}"
		return visita_string.format(self.caracter, self.vehiculo.modelo, self.vehiculo.anio, self.comentarios)

class Expediente(models.Model):

	vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)
	kilometraje = models.IntegerField()
	transmision = models.IntegerField()
	ult_visita = models.DateField()
	ult_aceite = models.DateField()
	prox_aceite = models.DateField()
	ult_frenos = models.DateField()
	prox_frenos = models.DateField()
	detalle_mecanico = models.TextField()
	detalle_pintura = models.TextField()
	detalle_electrico = models.TextField()
	detalle_suspension = models.TextField()
	detalle_direccion = models.TextField()

class Proceso(models.Model):

	nombre = models.CharField(max_length=100)
	caracter = models.CharField(max_length=100)
	descripcion = models.TextField()

class VisitaProceso(models.Model):

	visita = models.ForeignKey(Visita, on_delete=models.CASCADE)
	proceso = models.ForeignKey(Proceso, on_delete=models.CASCADE)

class Pieza(models.Model):

	nombre = models.CharField(max_length=100)
	descripcion = models.TextField()

class ProcesoPieza(models.Model):

	proceso = models.ForeignKey(Proceso,on_delete=models.CASCADE)
	pieza = models.ForeignKey(Pieza,on_delete=models.CASCADE)
	cantidad = models.IntegerField()

class ProcesoTecnico(models.Model):

	proceso = models.ForeignKey(Proceso,on_delete=models.CASCADE)
	tecnico = models.ForeignKey(Tecnico,on_delete=models.CASCADE)