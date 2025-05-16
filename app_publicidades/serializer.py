from rest_framework import serializers
from .models import Publicidad,Items_presupuesto_publicidades

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicidad
        fields = '__all__'




class DescripcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items_presupuesto_publicidades
        fields = '__all__'
