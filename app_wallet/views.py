import re
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import WalletSerializer
from .models import Wallet
from rest_framework.decorators import action
from django.db.models import Sum

from rest_framework.response import Response
# Create your views here.
class ViewWallet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer 

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Último restante_fondo
        ultimo = queryset.order_by('-id').values('restante_fondo').first()
        restante_actual = ultimo['restante_fondo'] if ultimo else None

        # Ingresos y su suma
        ingresos = queryset.filter(tipo_de_movimiento="CREDITO").values_list('monto', flat=True)
        total_ingresos = queryset.filter(tipo_de_movimiento="CREDITO").aggregate(total=Sum('monto'))['total'] or 0

        # Gastos y su suma
        gastos = queryset.filter(tipo_de_movimiento="DEBITO").values_list('monto', flat=True)
        total_gastos = queryset.filter(tipo_de_movimiento="DEBITO").aggregate(total=Sum('monto'))['total'] or 0

        return Response({
            "balance": restante_actual,
            "total_ingresos": total_ingresos,
            "total_gastos": total_gastos,
            "registros": serializer.data
        })
