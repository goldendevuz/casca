from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.models import BaseModel


class Barber(BaseModel):
    user = models.ForeignKey(
        to="accounts.User",
        on_delete=models.CASCADE,
        related_name="barber_profile",
        verbose_name=_("User"),
        help_text=_("The user account for the barber"),
    )
    barbershop = models.ForeignKey(
        to="barbershops.Barbershop",
        on_delete=models.CASCADE,
        related_name="barbers",
        verbose_name=_("Barbershop"),
        help_text=_("The barbershop this barber works at"),
    )

    class Meta:
        unique_together = ("user", "barbershop")
        ordering = ["-created"]
        verbose_name = _("Barber")
        verbose_name_plural = _("Barbers")

    def __str__(self):
        return f"{self.user} at {self.barbershop}"
