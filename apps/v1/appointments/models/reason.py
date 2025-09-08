from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.enums import ReasonTypes
from apps.v1.shared.models import BaseModel


class Reason(BaseModel):
    profile = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.CASCADE,
        related_name="reasons",
        verbose_name=_("Profile"),
        help_text=_("The profile that provided the reason"),
    )
    reason_type = models.CharField(
        verbose_name=_("Reason Type"),
        max_length=50,
        choices=ReasonTypes.choices,
        default=ReasonTypes.CHANGE_IN_PLANS,
        help_text=_("The type of reason provided"),
    )
    message = models.TextField(
        verbose_name=_("Message"),
        blank=True,
        null=True,
        help_text=_("Optional message describing the reason in more detail"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Reason")
        verbose_name_plural = _("Reasons")

    def __str__(self):
        return f"{self.profile} - {self.reason_type}"
