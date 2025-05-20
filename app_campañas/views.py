from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Head_campañas, Campañas_desc
from django.http import HttpResponse
from . serializer import Campanas_Serializer, Head_serializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, BooleanFilter
from app_dashboard.models import Dashboard
from rest_framework.response import Response
from django.db.models import Sum
from app_wallet.models import Wallet
from django.db.models import Count
from django.db.models.functions import TruncMonth
import calendar
from rest_framework.decorators import action
from collections import defaultdict



class HeadCampanasFilter(FilterSet):
    activa = BooleanFilter(field_name='activa', label='Está activa')

    class Meta:
        model = Head_campañas
        fields = ['activa']


class View_model_descripcion(viewsets.ModelViewSet):
    queryset = Campañas_desc.objects.all()
    serializer_class = Campanas_Serializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def resumencampanas(self, request):
        creditos_prpuesto = Wallet.objects.filter(tipo_de_movimiento='CREDITO')
        presupuesto_total = [l.monto for l in creditos_prpuesto]
        presupuesto = sum(presupuesto_total)

        inversion_total = Campañas_desc.objects.aggregate(inversion=Sum('inversion'))
        inversrion = inversion_total.get('inversion') or 0

        if presupuesto == 0:
            porcentaje = 0
        else:
            porcentaje = round(float(inversrion / presupuesto * 100), 2)

        presupuesto_formateado = f"{round(float(presupuesto), 2):,.2f}"
        inversion_formateado = f"{round(float(inversrion), 2):,.2f}"

        restante_presupuesto = Wallet.objects.order_by('-id').first()
        if restante_presupuesto:
            restante = f"{round(float(restante_presupuesto.restante_fondo), 2):,.2f}"
        else:
            restante = "0.00"



        valor = Campañas_desc.objects.annotate(
            mes=TruncMonth('fecha_pago')
        ).values('mes').annotate(
            total_cout=Sum('inversion')
        ).order_by('-total_cout')  # orden por el total

        if valor.exists():
            primero = valor.first()
            mes_fecha = primero['mes']  # datetime.date
            cuenta = primero['total_cout']
            numero_mes = mes_fecha.month
            nombre_mes = calendar.month_name[numero_mes].capitalize()
            datos = {"mes": nombre_mes, "Cuenta":cuenta}
        else:
            nombre_mes = "Sin datos"

      


        doc = defaultdict(lambda: [0]*12) 
        for mes in range(1, 13):
            inversiones = Campañas_desc.objects.filter(fecha_pago__month=mes)
            for c in inversiones:
                nombre = c.head_id.nombre_campañas
                inversion = c.inversion
                doc[nombre][mes - 1] += inversion 


        return Response({
            "presupuesto_total": presupuesto_formateado,
            "gastado": inversion_formateado,
            "porcentaje": porcentaje,
            "restante": restante,
            "campanas": doc,
            "mes_masfrecuente": datos
        })





class View_model_head(viewsets.ModelViewSet):
    
    queryset = Head_campañas.objects.all()
    serializer_class = Head_serializer

    







 