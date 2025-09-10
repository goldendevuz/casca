from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.v1.content.models import PrivacyPolicy
from apps.v1.content.serializers import PrivacyPolicySerializer


class PrivacyPolicyViewSet(ReadOnlyModelViewSet):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer
