from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from .models import Libro
def resumen(request):
 total = Libro.objects.count()
 return HttpResponse(f"Actualmente hay {total} libros registrados en labiblioteca.")

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Libro

@api_view(['GET'])
def listado_libros(request):
    libros = Libro.objects.all().order_by('id')

    paginador = PageNumberPagination()
    pagina = paginador.paginate_queryset(libros, request)

    datos = [
        {
            "id": libro.id,
            "titulo": libro.titulo,
            "autor": libro.autor.nombre,
            "precio": libro.precio,
            "disponible": libro.disponible,
            "descripcion": libro.titulo + ' escrito por ' + libro.autor.nombre,
        }
        for libro in pagina
    ]
    return paginador.get_paginated_response(datos)


from rest_framework import viewsets
from .models import Autor
from .serializers import AutorSerializer, LibroSerializer


# Diferencia entre PUT y PATCH:
# PUT actualiza el registro COMPLETO: hay que enviar todos los campos.
# PATCH actualiza solo UNA PARTE: se envían únicamente los campos que quieres cambiar.
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all().order_by('nombre')
    serializer_class = AutorSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all().order_by('titulo')
    serializer_class = LibroSerializer