from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .models import Libro
def resumen(request):
 total = Libro.objects.count()
 return HttpResponse(f"Actualmente hay {total} libros registrados en labiblioteca.")

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Libro

@api_view(['GET'])
def listado_libros(request):
    libros = Libro.objects.all()
    datos = [
        {
            "id": libro.id,
            "titulo": libro.titulo,
            "autor": libro.autor.nombre,
            "precio": libro.precio,
            "disponible": libro.disponible,
            'descripcion': libro.titulo + ' escrito por ' + libro.autor,
        }
        for libro in libros
    ]
    return Response(datos)


