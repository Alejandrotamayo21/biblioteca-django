from django.urls import path
from . import views

urlpatterns = [
    path('resumen/', views.resumen, name='resumen'),
    path('api/libros/', views.listado_libros, name='api_libros'),
]

