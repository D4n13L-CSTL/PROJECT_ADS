from rest_framework import serializers
from .models import Wallet

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = '__all__'
        
    def create(self, validated_data):

        validated_data['tipo_de_movimiento'] = validated_data['tipo_de_movimiento'].upper()
        
        return super().create(validated_data)