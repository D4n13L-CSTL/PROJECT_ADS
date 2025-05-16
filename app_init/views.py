from django.shortcuts import render
from .models import Prueba
from .serializer import PruebaSerilizada
from rest_framework import viewsets

def init(request):
    pass

class PruebaVies(viewsets.ModelViewSet):
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerilizada
    
    
