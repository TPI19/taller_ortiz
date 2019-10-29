from django.contrib import admin
from apps.taller.models import *

# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(Visita)
admin.site.register(Administrador)
admin.site.register(Especializacion)
admin.site.register(Tecnico)
admin.site.register(Cliente)
admin.site.register(Cita)
admin.site.register(Slot)
admin.site.register(Expediente)
admin.site.register(Proceso)
admin.site.register(Pieza)
admin.site.register(ProcesoPieza)
admin.site.register(ProcesoTecnico)