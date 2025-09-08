from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.models import BaseModel


class Mood(BaseModel):
    smile = models.ImageField(
        verbose_name=_("Smile"),
        upload_to="moods/",
        help_text=_("The image representing the mood"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Mood")
        verbose_name_plural = _("Moods")

    def __str__(self):
        return f"Mood {self.id}"
