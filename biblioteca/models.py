from django.db import models

# Create your models here.

from django.db import models
class Autor(models.Model):
 nombre = models.CharField(max_length=120)
 nacionalidad = models.CharField(max_length=60, blank=True)
 def __str__(self):
    return self.nombre
class Libro(models.Model):
 titulo = models.CharField(max_length=200)
 autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='libros')
 precio = models.DecimalField(max_digits=8, decimal_places=2)
 disponible = models.BooleanField(default=True)
 fecha_publicacion = models.DateField(null=True, blank=True)
 def __str__(self):
    return self.titulo
