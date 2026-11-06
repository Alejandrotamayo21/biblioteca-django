from rest_framework import serializers
from .models import Autor, Libro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'nacionalidad']

class LibroSerializer(serializers.ModelSerializer):
    autor_nombre = serializers.CharField(source='autor.nombre', read_only=True)

    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'autor_nombre', 'precio', 'disponible', 'fecha_publicacion']
    
#validate_<campo> valida un campo individual; validate (sin sufijo) recibe el diccionario completo y sirve para reglas que cruzan varios campos.
    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor que cero.")
        return value

    def validate(self, data):
        # Validación que involucra más de un campo a la vez
        if not data.get('disponible', True) and data.get('precio', 0) == 0:
            raise serializers.ValidationError("Un libro no disponible no puede tener precio 0.")
        return data






# Error común
#Llamar a serializer.save() sin haber llamado antes a serializer.is_valid() lanza una excepción. Siempre hay que validar primero; en las vistas de la sesión 9 y 10 usaremos is_valid(raise_exception=True) para que DRF devuelva automáticamente un error 400 con el detalle.
