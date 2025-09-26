from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.IntegerField(unique=True, default=None, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    deudor = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class Pago(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPago = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'Pago de {self.monto} por {self.cliente.nombre} el {self.fechaPago}'