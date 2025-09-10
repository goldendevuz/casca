from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.v1.notifications.views import NotificationListViewSet

router = DefaultRouter()
router.register(r'', NotificationListViewSet, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]
