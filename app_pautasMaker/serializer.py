from rest_framework import serializers
from .models import Pautas
from app_perfiles.models import Transacciones

class PautasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pautas
        fields = '__all__'
        
    def create(self, validated_data):
        validated_data['status_pauta'] = validated_data['status_pauta'].upper()
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        estado_anterior = instance.status_pauta
        estado_nuevo = validated_data.get('status_pauta', estado_anterior)

        # Primero actualizamos los valores del modelo
        instance = super().update(instance, validated_data)
        
        # Solo acreditamos si el estado cambió de PENDIENTE a otro
        if estado_nuevo == 'PROCESADA' and estado_anterior in ['PENDIENTE', 'ACTIVA']:
            modelo = instance.modelo
            wallet = modelo.Wallets  # related_name='Wallets'

            monto = instance.monto_de_pauta

            # Acreditar en la wallet
            wallet.save()

            # Registrar la transacción
            Transacciones.objects.create(
                wallet_id=wallet,
                tipo_de_movimiento='CREDITO',
                monto=monto
            )

        return instance


class PautaSerializer_front(serializers.ModelSerializer):
    class Meta:
        model = Pautas
        fields = ['nombre_pauta']
