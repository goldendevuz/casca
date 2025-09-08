from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.models import BaseModel


class Review(BaseModel):
    profile = models.ForeignKey(
        "accounts.Profile",
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=_("Profile"),
        help_text=_("The profile that wrote the review"),
    )
    appointment = models.ForeignKey(
        "appointments.Appointment",
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name=_("Appointment"),
        help_text=_("The appointment associated with the review"),
    )
    text = models.TextField(
        verbose_name=_("Text"),
        help_text=_("The content of the review"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return f"Review by {self.profile} for {self.appointment}"
