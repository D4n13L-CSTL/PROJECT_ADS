from django.db import models

# Create your models here.
class Wallet(models.Model):
    fecha_ingreso = models.DateField(auto_now_add=True)
    tipo_de_movimiento = models.CharField()
    monto = models.FloatField(null=True, blank=True,default=0.0)
    ultimo_monto = models.FloatField(default=0.0)
    restante_fondo = models.FloatField(null=True, default=0.0)
    
    
    def save(self, *args, **kwargs):
        # Solo establecer el ultimo_monto si el objeto es nuevo
        if not self.pk:
            # Obtener el último registro (por fecha de ingreso más reciente o por ID)
            ultimo_registro = Wallet.objects.order_by('-id').first()

            if ultimo_registro:
                self.ultimo_monto = ultimo_registro.restante_fondo
            else:
                self.ultimo_monto = 0.0  # Si no hay registros previos

        # Calcular el nuevo restante_fondo en base al tipo de movimiento
        if self.tipo_de_movimiento == 'CREDITO':
            self.restante_fondo = self.ultimo_monto + self.monto
        elif self.tipo_de_movimiento == 'DEBITO':
            self.restante_fondo = self.ultimo_monto - self.monto

        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'Wallet'
    
    