from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample

from apps.v1.settings.models import SecuritySetting


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Default Security Setting",
            summary="Defaults for a new security setting",
            value={
                "biometric_id": False,
                "face_id": False,
                "google_authenticator": False,
            },
            request_only=True,
            response_only=True,
        )
    ]
)
class SecuritySettingSerializer(serializers.ModelSerializer):
    biometric_id = serializers.BooleanField(default=False)
    face_id = serializers.BooleanField(default=False)
    google_authenticator = serializers.BooleanField(default=False)

    class Meta:
        model = SecuritySetting
        fields = "__all__"
        read_only_fields = ["profile"]
