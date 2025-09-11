from rest_framework import viewsets
from apps.v1.shared.models import Address
from apps.v1.shared.serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
