from rest_framework.viewsets import ReadOnlyModelViewSet
from apps.v1.content.models import Language
from apps.v1.content.serializers import LanguageSerializer


class LanguageViewSet(ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
