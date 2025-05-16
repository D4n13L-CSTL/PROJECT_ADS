import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

from rest_framework import serializers
from .models import Header_Modelos, tallas_modelos, TipoDeCuenta, SaldoAcumulado, Transacciones
from app_pautasMaker.serializer import PautaSerializer_front


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header_Modelos
        fields = '__all__'
        
    def create(self, validated_data):
        # Generar el código de wallet usando la cédula
        cedula = validated_data.get('cedula')
        nombres = validated_data.get('nombres').upper()
        apellidos = validated_data.get('apellidos').upper()
        codigo_wallet = f"M{cedula}"
        
        
        
        validated_data['nombres'] = nombres
        validated_data['apellidos'] = apellidos
        validated_data['codigo_wallet'] = codigo_wallet

        # Crear la instancia del modelo
        instance = Header_Modelos.objects.create(**validated_data)

        # Crear QR con los datos del modelo
        qr_data = f"{validated_data['codigo_wallet']}"
        qr_image = qrcode.make(qr_data)

        buffer = BytesIO()
        qr_image.save(buffer, format='PNG')
        image_file = ContentFile(buffer.getvalue(), name=f"qr_{instance.cedula}.png")

        instance.qr.save(image_file.name, image_file)
        instance.save()

        # Crear wallet asociado automáticamente
        SaldoAcumulado.objects.create(
            model_id=instance,
            codigo_wallet=codigo_wallet,
            saldo_disponible=0.0
        )

        return instance 
    










class Tallas(serializers.ModelSerializer):
    class Meta:
        model = tallas_modelos
        fields = '__all__'


class lista_de_modelosSerializer(serializers.ModelSerializer):
    modelo_id = HeaderSerializer()
    
    class Meta:
        model = tallas_modelos
        fields = '__all__'



        
    
class TipoDeCuentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDeCuenta
        fields = '__all__'

    def create(self, validated_data):
        
        iniciales = validated_data['cuenta'][0:2]

        validated_data['codigo'] = iniciales

        return super().create(validated_data)
    


class Wallets(serializers.ModelSerializer):
    class Meta:
        model = SaldoAcumulado
        fields = '__all__'




class TransccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacciones
        fields = '__all__'

    def create(self, validated_data):

        validated_data['tipo_de_movimiento'] = validated_data['tipo_de_movimiento'].upper()
        
        return super().create(validated_data)