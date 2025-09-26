from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import ClienteSerializer, PagoSerializer
from .models import Cliente, Pago

# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()

    #buscar cliente por campo
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nombre', 'documento','email']
    #buscar cliente por deudor
    filterset_fields = ['deudor']

class PagoViewSet(viewsets.ModelViewSet):
    serializer_class = PagoSerializer
    queryset = Pago.objects.all()

