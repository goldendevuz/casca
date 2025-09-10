from django.urls import path

from apps.v1.settings.views.security_setting import SecuritySettingUpdateView

urlpatterns = [
    path("security/", SecuritySettingUpdateView.as_view({"put": "update", "patch": "partial_update"})),
]
