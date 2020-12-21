from django.contrib import admin
from .models import Turno, Paciente, HistorialMedico, ObraSocial, MetodoPago, Estado, Producto
# Register your models here.
admin.site.register(Turno)
admin.site.register(Paciente)
admin.site.register(HistorialMedico)
admin.site.register(ObraSocial)
admin.site.register(MetodoPago)
admin.site.register(Estado)
admin.site.register(Producto)