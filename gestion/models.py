# gestion/models.py
from django.db import models

class Deporte(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    deporte = models.ForeignKey(Deporte, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True)
    localidad = models.CharField(max_length=100)
    barrio = models.CharField(max_length=100)
    precioHora = models.DecimalField(max_digits=10, decimal_places=2)
    fotoUrl = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nombre