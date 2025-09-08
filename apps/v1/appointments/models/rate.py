from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.models import BaseModel


class Rate(BaseModel):
    profile = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.CASCADE,
        related_name="rates",
        verbose_name=_("Profile"),
        help_text=_("The profile that gave the rating"),
    )
    review = models.ForeignKey(
        to="appointments.Review",
        on_delete=models.CASCADE,
        related_name="rates",
        verbose_name=_("Review"),
        help_text=_("The review that is being rated"),
    )
    value = models.SmallIntegerField(
        verbose_name=_("Value"),
        help_text=_("The rating value given"),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["profile", "review"],
                name="unique_rate_per_review"
            )
        ]
        ordering = ["-created"]
        verbose_name = _("Rate")
        verbose_name_plural = _("Rates")

    def __str__(self):
        return f"{self.profile} rated {self.review} with {self.value}"
