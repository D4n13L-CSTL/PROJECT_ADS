from rest_framework import serializers
from .models import Publicidad,Items_presupuesto_publicidades

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicidad
        fields = ['id','nombre', 'activa']




class DescripcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items_presupuesto_publicidades
        fields = '__all__'


class SerializerItems(serializers.ModelSerializer):
    nombre_publicidad = serializers.CharField(source ='id_publicidad.nombre', read_only = True)
    activa_publicidad = serializers.BooleanField(source='id_publicidad.activa', read_only=True)
    id_publicidad = serializers.IntegerField(source='id_publicidad.id', read_only=True)
    class Meta:
        model = Items_presupuesto_publicidades
        fields = ['datos', 'nombre_publicidad', 'activa_publicidad', 'id_publicidad']