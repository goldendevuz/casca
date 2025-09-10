from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.v1.notifications.views import NotificationListViewSet, UserNotificationListViewSet

router = DefaultRouter()
router.register(r'user', UserNotificationListViewSet, basename='user-notification')
router.register(r'', NotificationListViewSet, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]
