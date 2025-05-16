from django.shortcuts import render
from rest_framework import viewsets
from .serializer import HeaderSerializer, DescripcionesSerializer
from .models import Publicidad, Items_presupuesto_publicidades
# Create your views here.

class HeaderViewSet(viewsets.ModelViewSet):
    queryset = Publicidad.objects.all()
    serializer_class = HeaderSerializer

class DescripcionesViewSet(viewsets.ModelViewSet):
    queryset = Items_presupuesto_publicidades.objects.all()
    serializer_class = DescripcionesSerializer

