from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer

from apps.v1.notifications.models import Notification


class NotificationSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Notification)

    class Meta:
        model = Notification
        fields = "__all__"
