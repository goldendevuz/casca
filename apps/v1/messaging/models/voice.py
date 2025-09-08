from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.models import BaseModel


class Voice(BaseModel):
    file = models.FileField(
        verbose_name=_("File"),
        upload_to="voices/",
        help_text=_("The voice/audio file"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Voice")
        verbose_name_plural = _("Voices")

    def __str__(self):
        return f"Voice file {self.id}"
