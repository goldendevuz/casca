from rest_framework import mixins, viewsets

from apps.v1.notifications.models import Notification
from apps.v1.notifications.serializers import NotificationSerializer


class NotificationListViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
