from rest_framework import mixins, viewsets

from apps.v1.notifications.models import NotificationSetting
from apps.v1.notifications.serializers import NotificationSettingSerializer


class NotificationSettingViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = NotificationSettingSerializer

    def get_object(self):
        # always return current user's notification settings
        return NotificationSetting.objects.get(profile=self.request.user.profile) # noqa
