from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from apps.v1.notifications.models import UserNotification
from apps.v1.notifications.serializers import UserNotificationSerializer


class UserNotificationListViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = UserNotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UserNotification.objects.filter(profile__user=self.request.user)
