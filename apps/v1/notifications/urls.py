from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.v1.notifications.views import NotificationListViewSet, UserNotificationListViewSet, NotificationSettingViewSet

router = DefaultRouter()
router.register(r'user', UserNotificationListViewSet, basename='user-notification')
router.register(r'', NotificationListViewSet, basename='notification')

urlpatterns = [
    path(
        "settings/",
        NotificationSettingViewSet.as_view({"get": "retrieve", "patch": "partial_update"}),
        name="notification-settings"
    ),
    path('', include(router.urls)),
]
