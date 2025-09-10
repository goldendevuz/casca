from rest_framework import serializers
from parler_rest.fields import TranslatedFieldsField
from parler_rest.serializers import TranslatableModelSerializer

from apps.v1.notifications.models import Notification, UserNotification


class NotificationNestedSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Notification)

    class Meta:
        model = Notification
        fields = ["id", "icon", "translations"]


class UserNotificationSerializer(serializers.ModelSerializer):
    notification = NotificationNestedSerializer(read_only=True)

    class Meta:
        model = UserNotification
        fields = ["id", "notification", "state", "sent_at"]
