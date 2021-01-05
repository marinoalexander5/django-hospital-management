from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import User
from django.conf import settings
from localflavor.ar.forms import ARDNIField

# Create your models here.
class ObraSocial(models.Model):
    alias = models.CharField(max_length=50)

    def __str__(self):
        return self.alias

class Paciente(models.Model):
    nombre = models.CharField(max_length=50, validators=[MinLengthValidator(2, "El nombre debe contener al menos 2 caracteres")])
    apellido = models.CharField(max_length=50, validators=[MinLengthValidator(2, "El apellido debe contener al menos 2 caracteres")])
    dni = ARDNIField(max_length=10, min_length=7)
    fecha_nacimiento= models.DateField()
    email = models.EmailField()
    telefono = models.CharField(max_length=17)
    direccion = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    obra_social = models.ForeignKey(ObraSocial, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.apellido}, {self.nombre}'


class Turno(models.Model):
    fecha = models.DateTimeField(auto_now=False, auto_now_add=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False)
    profesional_medico = models.ForeignKey(settings.AUTH_USER_MODEL, limit_choices_to={'groups__name': 'Personal Medico' }, on_delete=models.CASCADE, null=False)


class HistorialMedico(models.Model):
    fecha = models.DateField(auto_now=True)
    descripcion = models.TextField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return  f'historial medico {self.paciente}'

class MetodoPago(models.Model):
    metodo = models.CharField(max_length=50)


class Estado(models.Model):
    estado = models.CharField(max_length=50)


class Pedido(models.Model):
    # productos = models.ManyToManyField('Productos', through='Paciente')
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    subtotal = models.DecimalField(max_digits=5, decimal_places=2)
    metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    estado_pedido = models.ForeignKey(Estado, on_delete=models.CASCADE)
   

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    # pedidos = models.ManyToManyField('ProfesionalMedico', through='Paciente')


    # def __str__(self):
    #     return self.nombre

    # class Especialidades(models.Model):
#     especialidad = models.CharField(max_length=200)

#     def __str__(self):
#         return self.especialidad


# class ProfesionalMedico(models.Model):
#     medico = models.ForeignKey(User, limit_choices_to={'is_staff': True}, on_delete=models.CASCADE, null=True)
#     nombre = models.CharField(max_length=50, validators=[MinLengthValidator(2, "El nombre debe contener al menos 2 caracteres")])
#     apellido = models.CharField(max_length=50, validators=[MinLengthValidator(2, "El apellido debe contener al menos 2 caracteres")])
#     especialidad =  models.ForeignKey(Especialidades, on_delete=models.CASCADE, null=False)
#     pacientes = models.ManyToManyField('Paciente', through='Cabecera')

#     def __str__(self):
#         return (f'{self.apellido}, {self.nombre}')
