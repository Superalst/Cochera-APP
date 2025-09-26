from django.urls import path, include
from rest_framework import routers
from .views import ClienteViewSet, PagoViewSet

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'pagos', PagoViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]