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

    
    @action(detail=False, methods=['get'])
    def header(self,request):
        activas = Publicidad.objects.filter(activa=True).values().count()
        
        pendientes = Publicidad.objects.filter(activa=False).values().count()

        return Response({"Activas":activas,
                         "Pendientes":pendientes})
    
    


class DescripcionesViewSet(viewsets.ModelViewSet):
    queryset = Items_presupuesto_publicidades.objects.all()
    serializer_class = DescripcionesSerializer
    
    @action(detail=False, methods=['get'])
    def datos(self,request):
        id_publicidad = request.query_params.get('id')
        
        queryset  = Items_presupuesto_publicidades.objects.all()
        
        
        if id_publicidad:
            queryset = queryset.filter(id_publicidad = id_publicidad)

        serializer  = SerializerItems(queryset, many=True)
        
        return Response(serializer.data)


    
    