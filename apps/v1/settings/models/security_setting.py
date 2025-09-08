from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.models import BaseModel


class SecuritySetting(BaseModel):
    profile = models.ForeignKey(
        "users.Profile",
        on_delete=models.CASCADE,
        related_name="security_settings",
        verbose_name=_("Profile"),
        help_text=_("The profile this security setting belongs to"),
    )
    biometric_id = models.BooleanField(
        verbose_name=_("Biometric ID"),
        default=False,
        help_text=_("Whether biometric ID authentication is enabled"),
    )
    face_id = models.BooleanField(
        verbose_name=_("Face ID"),
        default=False,
        help_text=_("Whether Face ID authentication is enabled"),
    )
    google_authenticator = models.BooleanField(
        verbose_name=_("Google Authenticator"),
        default=False,
        help_text=_("Whether Google Authenticator is enabled"),
    )

    class Meta:
        verbose_name = _("Security Setting")
        verbose_name_plural = _("Security Settings")

    def __str__(self):
        return f"Security settings for {self.profile}"
