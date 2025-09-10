from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.enums import NotificationStates
from apps.v1.shared.models import BaseModel


class UserNotification(BaseModel):
    profile = models.ForeignKey(
        to="accounts.Profile",
        on_delete=models.CASCADE,
        related_name="user_notifications",
        verbose_name=_("Profile"),
        help_text=_("The profile that receives this notification"),
    )
    notification = models.ForeignKey(
        to="content.Notification",
        on_delete=models.CASCADE,
        related_name="user_notifications",
        verbose_name=_("Notification"),
        help_text=_("The base notification being sent to the user"),
    )
    state = models.CharField(
        verbose_name=_("State"),
        max_length=10,
        choices=NotificationStates.choices,
        default=NotificationStates.NEW,
        help_text=_("The current state of the notification"),
    )
    sent_at = models.DateTimeField(
        verbose_name=_("Sent At"),
        default=timezone.now,
        help_text=_("The datetime when the notification was sent"),
    )

    class Meta:
        ordering = ["-sent_at"]
        verbose_name = _("User Notification")
        verbose_name_plural = _("User Notifications")

    def __str__(self):
        return str(self.notification)
