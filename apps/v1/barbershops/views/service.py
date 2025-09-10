from rest_framework import viewsets

from apps.v1.barbershops.models import Service
from apps.v1.barbershops.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
