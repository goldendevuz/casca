from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from apps.v1.settings.models import SecuritySetting
from apps.v1.settings.serializers import SecuritySettingSerializer


class SecuritySettingUpdateView(
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = SecuritySettingSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # return the current user's security setting
        return SecuritySetting.objects.get(profile__user=self.request.user)
