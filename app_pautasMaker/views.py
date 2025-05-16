from django.shortcuts import render
from rest_framework import viewsets
from .models import Pautas
from .serializer import PautasSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class PautasView(viewsets.ModelViewSet):
    queryset = Pautas.objects.all()
    serializer_class = PautasSerializer
    @action(detail=False, methods=['get'])
    def general(self,request):
        total_pendientes = Pautas.objects.filter(status_pauta='PENDIENTE').count()
        total_activas = Pautas.objects.filter(status_pauta='ACTIVA').count()
        total_procesadas = Pautas.objects.filter(status_pauta='PROCESADA').count()

        
        lista_pautas = Pautas.objects.select_related('modelo').all()

        lista_pautas_serializadas = [
            {
                "id_pauta":pauta.id,
                "fecha": pauta.fecha,
                "nombre_pauta": pauta.nombre_pauta,
                "ubicacion_pauta": pauta.ubicacion_pauta,
                "autorizacio_comercial": pauta.autorizacio_comercial,
                "autorizacion_directiva": pauta.autorizacion_directiva,
                "monto_de_pauta": pauta.monto_de_pauta,
                "status_pauta": pauta.status_pauta,
                "modelo": pauta.modelo.nombres , # Aquí pones el nombre, no el ID
                "id_modelo":pauta.modelo.id
        }
            for pauta in lista_pautas
            
        ]

        total_inversion = Pautas.objects.values('monto_de_pauta')
        
        
        suma_inversion = sum([i['monto_de_pauta'] for i in total_inversion])
        
        return Response({"pendientes":total_pendientes, 'activas':total_activas, "inversion_Total":suma_inversion,"total_procesadas":total_procesadas,"lista_pautas":lista_pautas_serializadas})

