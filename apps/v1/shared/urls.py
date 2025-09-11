from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.v1.shared.views import AddressViewSet

router = DefaultRouter()
router.register(r'addresses', AddressViewSet, basename='address')

urlpatterns = [
    path('', include(router.urls)),
]
