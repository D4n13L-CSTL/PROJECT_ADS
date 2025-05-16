from django.shortcuts import render
from rest_framework import viewsets
from .models import Header_Modelos, tallas_modelos, TipoDeCuenta, SaldoAcumulado, Transacciones
from .serializer import HeaderSerializer, Tallas,  TipoDeCuentaSerializer, Wallets, TransccionesSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count

class HeaderModelos(viewsets.ModelViewSet):
    queryset = Header_Modelos.objects.all()
    serializer_class = HeaderSerializer


    @action(detail=False, methods=['get'])
    def modelos(self,request):
        modelos = tallas_modelos.objects.select_related('modelo_id').values(
            'camisa',
            'pantalon',
            'zapatos',
            'modelo_id__id',
            'modelo_id__nombres',
            'modelo_id__apellidos'
            )
        
        
        talla_comun = tallas_modelos.objects.values('camisa').annotate(total=Count('camisa')).order_by('-total').first()
        
        
        total_modelo = Header_Modelos.objects.values('nombres').count()
        return Response({"lista_de_modelos":modelos, "total_modelos":total_modelo, 'talla_mas_comun':talla_comun})

    @action(detail=False, methods=['get'])
    def detallespersonales(self, request):
        id_model = request.query_params.get('id')

        
                
        lista_detalles_fron = SaldoAcumulado.objects.select_related('model_id').all()
        
        if id_model:
            lista_detalles_fron = lista_detalles_fron.filter(model_id=id_model)
            

        
        lista_front = [{'id':i.model_id.id,
                        'nombre':i.model_id.nombres,
                        "apellidos":i.model_id.apellidos,
                        "cedula":i.model_id.cedula,
                        "correo":i.model_id.correo,
                        "telefono":i.model_id.numero_tlf,
                        "edad":i.model_id.edad,
                        "tipo_de_cuenta":i.model_id.tipo_de_cuenta.cuenta,
                        "id_tipo_cuenta":i.model_id.tipo_de_cuenta.id,
                        "codigo_wallet":i.model_id.codigo_wallet,
                        "saldo":i.saldo_disponible,
                        "qr": request.build_absolute_uri(i.model_id.qr.url) if i.model_id.qr else None,  # Genera la URL completa
                        "pautas_asignadas":{"nombres": [pautas.nombre_pauta for pautas in i.model_id.pautas_asignadas.all()]
}
                        } for i in lista_detalles_fron]
        
        

        

        return Response({"Detalles": lista_front})    
    
    
class TallasModelos(viewsets.ModelViewSet):
    queryset = tallas_modelos.objects.all()
    serializer_class = Tallas


class TipoDeCuentaView(viewsets.ModelViewSet):
    queryset = TipoDeCuenta.objects.all()
    serializer_class = TipoDeCuentaSerializer
    

class WalletsModelView(viewsets.ModelViewSet):
    queryset = SaldoAcumulado.objects.all()
    serializer_class = Wallets
    @action(detail=False, methods=['get'])
    def detalleswallet(self,request):
        
        
        datos = SaldoAcumulado.objects.all().values()
        return Response({"Detalles":datos})



class TranaccionesModelView(viewsets.ModelViewSet):
    queryset = Transacciones.objects.all()
    serializer_class = TransccionesSerializer


