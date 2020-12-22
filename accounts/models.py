from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    SECRETARIA = 1
    PERSONAL_MEDICO = 2
    VENTAS = 3
    TALLER = 4
    GERENCIA = 5

    ROLE_CHOICES = (
        (SECRETARIA, 'Secretaria'),
        (PERSONAL_MEDICO, 'Personal Medico'),
        (VENTAS, 'Ventas'),
        (TALLER, 'Taller'),
        (GERENCIA, 'Gerencia'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.get_id_display()

class User(AbstractUser):
    role = models.ManyToManyField(Role)