from django.shortcuts import render
from rest_framework import viewsets
from .serializer import HeaderSerializer, DescripcionesSerializer, SerializerItems
from .models import Publicidad, Items_presupuesto_publicidades
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class HeaderViewSet(viewsets.ModelViewSet):
    queryset = Publicidad.objects.all()
    serializer_class = HeaderSerializer

class DescripcionesViewSet(viewsets.ModelViewSet):
    queryset = Items_presupuesto_publicidades.objects.all()
    serializer_class = DescripcionesSerializer
    
    @action(detail=False, methods=['get'])
    def datos(self,request):
        queryset  = Items_presupuesto_publicidades.objects.all()
        serializer_class = SerializerItems(queryset, many=True)

        return Response(serializer_class.data)
