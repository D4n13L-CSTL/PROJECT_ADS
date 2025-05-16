from django.db import models

# Create your models here.
class Head_campañas(models.Model):
    nombre_campañas = models.CharField(max_length=50)
    fecha_creacion = models.DateField(auto_now_add=True)
    activa = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre_campañas

    class Meta:
        db_table = "Head_campanas" 


class Campañas_desc(models.Model):
    fecha_pago = models.DateField()
    tipo_evento = models.CharField(max_length=50)
    tipo_contendido = models.CharField(max_length=50)
    duracion = models.IntegerField()
    alcance = models.IntegerField()
    inversion = models.FloatField()
    head_id = models.ForeignKey(Head_campañas, on_delete=models.CASCADE)
    

    class Meta:
        db_table = "Campanas_descri"


