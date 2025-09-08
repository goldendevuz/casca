from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.models import BaseModel


class Message(BaseModel):
    owner = models.ForeignKey(
        "accounts.Profile",
        on_delete=models.CASCADE,
        related_name="sent_messages",
        verbose_name=_("Owner"),
        help_text=_("The profile that sent the message"),
    )
    receiver = models.ForeignKey(
        "accounts.Profile",
        on_delete=models.CASCADE,
        related_name="received_messages",
        verbose_name=_("Receiver"),
        help_text=_("The profile that receives the message"),
    )
    text = models.TextField(
        verbose_name=_("Text"),
        blank=True,
        null=True,
        help_text=_("The text content of the message"),
    )
    voice = models.ForeignKey(
        "messaging.Voice",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="messages",
        verbose_name=_("Voice"),
        help_text=_("The voice/audio attached to the message"),
    )
    encrypted = models.BooleanField(
        verbose_name=_("Encrypted"),
        default=False,
        help_text=_("Whether the message is encrypted"),
    )

    class Meta:
        ordering = ["-created"]
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

    def __str__(self):
        return f"Message from {self.owner} to {self.receiver}"
