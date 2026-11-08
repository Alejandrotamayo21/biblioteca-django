from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('autores', views.AutorViewSet, basename='autor')
router.register('libros', views.LibroViewSet, basename='libro')

urlpatterns = [
    path('resumen/', views.resumen, name='resumen'),
    path('libros/disponibles/', views.LibroDisponibleAPIView.as_view(), name='libros_disponibles'),
    path('libros/disponibles-generic/', views.LibroDisponibleGenericView.as_view(), name='libros_disponibles_generic'),
    path('', include(router.urls)),
]