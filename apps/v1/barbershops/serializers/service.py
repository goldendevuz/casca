from parler_rest.serializers import TranslatableModelSerializer

from apps.v1.barbershops.models import Service


class ServiceSerializer(TranslatableModelSerializer):
    class Meta:
        model = Service
        fields = ("name",)
