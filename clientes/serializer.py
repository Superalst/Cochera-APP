from rest_framework import serializers
from .models import Cliente, Pago

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'



class ClienteSerializer(serializers.ModelSerializer):
    pagos= PagoSerializer(many=True, read_only=True)
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'documento', 'email', 'telefono', 'direccion', 'deudor', 'pagos']