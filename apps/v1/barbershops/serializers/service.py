from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from apps.v1.barbershops.models import Service


class ServiceSerializer(TranslatableModelSerializer):
    # translations = TranslatedFieldsField(shared_model=Service)

    class Meta:
        model = Service
        fields = ("name",)
