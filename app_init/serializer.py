from rest_framework import serializers
from .models import Prueba

class PruebaSerilizada(serializers.ModelSerializer):
    class Meta:
        model = Prueba
        fields = '__all__'