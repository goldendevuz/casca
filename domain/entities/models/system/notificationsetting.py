from django.db import models

from config.settings.base import AUTH_USER_MODEL
from domain.entities.models.shared import BaseModel


class NotificationSetting(BaseModel):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notification_settings')
    general = models.BooleanField(default=True)
    sound = models.BooleanField(default=True)
    vibrate = models.BooleanField(default=True)
    special_offers = models.BooleanField(default=True)
    promo_and_discount = models.BooleanField(default=True)
    payments = models.BooleanField(default=True)
    cashback = models.BooleanField(default=True)
    app_updates = models.BooleanField(default=True)
    new_service = models.BooleanField(default=True)
    new_tips = models.BooleanField(default=True)

    def __str__(self):
        return f"Notification Settings for {self.user}"
