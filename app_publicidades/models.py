from django.db import models

# Create your models here.
class Publicidad(models.Model):
    nombre  = models.CharField(max_length=100, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, blank=True, null=True)
    activa = models.BooleanField(default=False)
    
    

    class Meta:
        db_table = "Publicidad" 

    def __str__(self):
        return self.nombre


class Items_presupuesto_publicidades(models.Model):
    
    nombre_item= models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    monto_item = models.CharField(max_length=50, blank=True, null=True)
    id_publicidad = models.ForeignKey(Publicidad, on_delete=models.CASCADE )
    
    class Meta:
        db_table = "Items_presupuesto_publicidades"
        
