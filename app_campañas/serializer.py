from rest_framework import serializers
from .models import Head_campañas, Campañas_desc
from app_dashboard.models import Dashboard
from app_perfiles.models import Header_Modelos
from app_wallet.models import Wallet
class Head_serializer(serializers.ModelSerializer):
    class Meta:
        model = Head_campañas
        fields = '__all__'
        
class Campanas_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Campañas_desc
        fields = '__all__'
        
    def create(self, validated_data):
        
        inversion = validated_data.get('inversion', 0.0)
        
        campa = Campañas_desc.objects.create(**validated_data)
        
        
        Wallet.objects.create(
            tipo_de_movimiento = 'DEBITO',
            monto = inversion
            )

        return campa
    
    
    
    