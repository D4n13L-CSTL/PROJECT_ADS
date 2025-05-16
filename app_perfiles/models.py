from django.db import models



# Create your models here.

class TipoDeCuenta(models.Model):
    cuenta = models.CharField(max_length=50, blank=True, null=True)
    codigo = models.CharField(max_length=5, null=True)
    def __str__(self):
        return self.cuenta
    
    class Meta:
        db_table = "TipoDeCuenta"

class Header_Modelos(models.Model):
    nombres  = models.CharField(max_length=100, blank=True, null=True)
    apellidos  = models.CharField(max_length=100, blank=True, null=True)
    correo = models.EmailField(max_length=100, blank=True, null=True)
    cedula  = models.CharField(max_length=100, blank=True, null=True)
    numero_tlf = models.CharField(max_length=15, blank=True, null=True)
    edad = models.IntegerField(null=True)
    qr = models.ImageField(upload_to='qrcodes/', blank=True, null=True)
    codigo_wallet = models.CharField(max_length=50, blank=True, null=True)
    tipo_de_cuenta  = models.ForeignKey(TipoDeCuenta, on_delete=models.CASCADE)
    

    class Meta:
        db_table = "Header_Modelos" 
    
    def __str__(self): 
        return self.nombres + ' ' + self.apellidos


class tallas_modelos(models.Model):
    camisa  = models.CharField(max_length=100, blank=True, null=True)
    pantalon  = models.CharField(max_length=100, blank=True, null=True)
    zapatos  = models.CharField(max_length=100, blank=True, null=True)
    vestimenta  = models.CharField(max_length=100, blank=True, null=True)
    modelo_id = models.ForeignKey(Header_Modelos, on_delete=models.CASCADE )
    
    
    class Meta:
        db_table = "tallas_modelos"
        


class SaldoAcumulado(models.Model):
    saldo_disponible = models.FloatField(default=0.0)
    codigo_wallet = models.CharField(max_length=20, null=True)
    model_id = models.OneToOneField(Header_Modelos, on_delete=models.CASCADE, related_name='Wallets', null=True)

    class Meta:
        db_table = "WalletModelos"
    
    def __str__(self):
        return self.codigo_wallet
    

class Transacciones(models.Model):
    fecha = models.DateField(auto_now_add=True)
    tipo_de_movimiento = models.CharField(max_length=20)
    monto = models.FloatField(default=0.0)
    wallet_id = models.ForeignKey(SaldoAcumulado, on_delete=models.CASCADE, related_name='Transacciones')

    def save(self, *args, **kwargs):
        if self.pk is None:  # Solo si es nueva transacción
            if self.tipo_de_movimiento == 'CREDITO':
                self.wallet_id.saldo_disponible += self.monto
            elif self.tipo_de_movimiento == 'DEBITO':
                if self.wallet_id.saldo_disponible < self.monto:
                    raise ValueError("Saldo insuficiente")
                self.wallet_id.saldo_disponible -= self.monto
            else:
                raise ValueError("Tipo de movimiento inválido")

            self.wallet_id.save()
        
        super().save(*args, **kwargs)
    class Meta:
        db_table = "TransccionesWalletsModelos"