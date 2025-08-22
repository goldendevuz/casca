from django.db import models

from config.settings.base import AUTH_USER_MODEL
from domain.entities.models.shared import BaseModel



class SecuritySetting(BaseModel):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='security_settings')
    remember_me = models.BooleanField(default=False)
    face_id = models.BooleanField(default=False)
    biometric_id = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Security Setting"
        verbose_name_plural = "Security Settings"
        app_label = "infrastructure"

    def __str__(self):
        return f"Security Settings for {self.user}"