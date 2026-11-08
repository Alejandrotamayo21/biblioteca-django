from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('autores', views.AutorViewSet, basename='autor')
router.register('libros', views.LibroViewSet, basename='libro')

urlpatterns = [
    path('resumen/', views.resumen, name='resumen'),
    path('', include(router.urls)),
]