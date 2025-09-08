from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.models import BaseModel


class DonateToBarber(BaseModel):
    profile = models.ForeignKey(
        "users.Profile",
        on_delete=models.CASCADE,
        related_name="donations",
        verbose_name=_("Profile"),
        help_text=_("The profile that made the donation"),
    )
    barber = models.ForeignKey(
        "barbers.Barber",
        on_delete=models.CASCADE,
        related_name="donations",
        verbose_name=_("Barber"),
        help_text=_("The barber receiving the donation"),
    )
    amount = models.PositiveIntegerField(
        verbose_name=_("Amount"),
        help_text=_("The amount donated"),
    )
    payment = models.ForeignKey(
        "payments.Payment",
        on_delete=models.CASCADE,
        related_name="donations",
        verbose_name=_("Payment"),
        help_text=_("The payment used for the donation"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Donate to Barber")
        verbose_name_plural = _("Donations to Barbers")

    def __str__(self):
        return f"{self.profile} donated {self.amount} to {self.barber}"
