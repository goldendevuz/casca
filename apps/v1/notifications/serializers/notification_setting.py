from rest_framework import serializers

from apps.v1.notifications.models import NotificationSetting


class NotificationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSetting
        fields = "__all__"
        read_only_fields = ["profile"]
