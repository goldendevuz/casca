from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.models import BaseModel


class Bookmark(BaseModel):
    profile = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.CASCADE,
        related_name="bookmarks",
        verbose_name=_("Profile"),
        help_text=_("The profile that created the bookmark"),
    )
    barbershop = models.ForeignKey(
        to="barbershops.Barbershop",
        on_delete=models.CASCADE,
        related_name="bookmarks",
        verbose_name=_("Barbershop"),
        help_text=_("The barbershop that was bookmarked"),
    )

    class Meta:
        unique_together = ("profile", "barbershop")
        ordering = ["-created"]
        verbose_name = _("Bookmark")
        verbose_name_plural = _("Bookmarks")

    def __str__(self):
        return f"{self.profile} → {self.barbershop}"
