from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.v1.payments.models import PromotionCategory
from apps.v1.payments.serializers.promotion_category import (
    PromotionCategorySerializer,
    PromotionCategoryListSerializer,
)


class PromotionCategoryViewSet(viewsets.ModelViewSet):
    """ViewSet for managing promotion categories"""

    queryset = PromotionCategory.objects.all()
    serializer_class = PromotionCategorySerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PromotionCategoryListSerializer
        return PromotionCategorySerializer

    @action(detail=False, methods=["get"])
    def active(self, request):
        """Get only active categories"""
        qs = self.get_queryset().filter(is_active=True)
        serializer = PromotionCategoryListSerializer(qs, many=True, context={"request": request})
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def promotions(self, request, pk=None):
        """Get promotions under this category"""
        category = self.get_object()
        promotions = category.promotions.all()
        from apps.v1.payments.serializers.promotion import PromotionListSerializer
        serializer = PromotionListSerializer(promotions, many=True, context={"request": request})
        return Response(serializer.data)
