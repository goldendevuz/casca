from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.models import BaseModel


class MessageStatus(BaseModel):
    message = models.ForeignKey(
        "messages.Message",
        on_delete=models.CASCADE,
        related_name="statuses",
        verbose_name=_("Message"),
        help_text=_("The message this status refers to"),
    )
    user = models.ForeignKey(
        "users.Profile",
        on_delete=models.CASCADE,
        related_name="message_statuses",
        verbose_name=_("User"),
        help_text=_("The user this status belongs to"),
    )
    is_read = models.BooleanField(
        verbose_name=_("Is Read"),
        default=False,
        help_text=_("Whether the message has been read by the user"),
    )
    is_played = models.BooleanField(
        verbose_name=_("Is Played"),
        default=False,
        help_text=_("Whether the message media has been played by the user"),
    )
    updated_at = models.DateTimeField(
        verbose_name=_("Updated At"),
        null=True,
        blank=True,
        help_text=_("Timestamp when the status was last updated"),
    )

    class Meta:
        unique_together = ("message", "user")
        ordering = ["-updated_at", "-created"]
        verbose_name = _("Message Status")
        verbose_name_plural = _("Message Statuses")

    def __str__(self):
        return f"Status of {self.message} for {self.user}"
