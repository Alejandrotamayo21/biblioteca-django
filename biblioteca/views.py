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





# - Clase#8: APIView y Generic Views -
# Regla de negocio: solo mostrar los libros que están disponibles.
from rest_framework.views import APIView
from rest_framework import status, generics


# Versión 1: APIView (manual)
class LibroDisponibleAPIView(APIView):
    """Devuelve solo los libros marcados como disponibles."""

    def get(self, request):
        libros = Libro.objects.filter(disponible=True).order_by('titulo')
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = LibroSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Versión 2: Generic View (varita magica )
class LibroDisponibleGenericView(generics.ListCreateAPIView):
    serializer_class = LibroSerializer
    pagination_class = None  # sin paginación, para que el resultado sea igual al del APIView

    def get_queryset(self):
        return Libro.objects.filter(disponible=True).order_by('titulo')


# Comparación: el APIView tiene 11 líneas de código dentro de la clase
# y la Generic View solo 5, así que la Generic View ahorra 6 líneas.