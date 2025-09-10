from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField

from apps.v1.content.models import PrivacyPolicy


class PrivacyPolicySerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=PrivacyPolicy)

    class Meta:
        model = PrivacyPolicy
        fields = "__all__"
