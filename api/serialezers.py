from .models import Empleados
from rest_framework import serializers

class EmpleadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleados
        fields = ('id', 'identificacion', 'nombres',
                    'apellidos', 'correo', 'salario', 'activo')
        #read_only_fields = ('id',)

    