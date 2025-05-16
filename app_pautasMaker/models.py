from django.db import models
from app_perfiles.models import Header_Modelos
# Create your models here.

class Pautas(models.Model):
    fecha = models.DateField()
    modelo = models.ForeignKey(Header_Modelos, on_delete=models.CASCADE, related_name='pautas_asignadas')
    nombre_pauta = models.CharField(max_length=50)
    ubicacion_pauta = models.CharField(max_length=50)
    autorizacio_comercial = models.BooleanField(default=False, null=True)
    autorizacion_directiva = models.BooleanField(default=False)
    monto_de_pauta = models.FloatField(default=0.0)
    status_pauta = models.CharField(default='PENDIENTE')
    
    class Meta:
        db_table = 'Pautas'