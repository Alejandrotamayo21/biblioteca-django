from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Libro
def resumen(request):
 total = Libro.objects.count()
 return HttpResponse(f"Actualmente hay {total} libros registrados en labiblioteca.")