from django.db import models
from app_campañas.models import Campañas_desc
from app_perfiles.models import Header_Modelos

# Create your models here.
class Dashboard(models.Model):
    total_campañas = models.FloatField()
    campanas_activa = models.IntegerField()
    Cantidad_modelos = models.IntegerField()
    
