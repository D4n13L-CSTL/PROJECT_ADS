from rest_framework import serializers
from .models import Publicidad,Items_presupuesto_publicidades

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicidad
        fields = ['id','nombre']




class DescripcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items_presupuesto_publicidades
        fields = '__all__'


class SerializerItems(serializers.ModelSerializer):
    nombre_publicidad = serializers.CharField(source ='id_publicidad.nombre', read_only = True)
    class Meta:
        model = Items_presupuesto_publicidades
        fields = ['datos', 'nombre_publicidad']