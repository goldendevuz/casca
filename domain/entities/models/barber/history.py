from django.db import models

from domain.entities.models.shared import BaseModel
from . import Barber

class History(BaseModel):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='history_logs')
    action = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "History"
        verbose_name_plural = "Histories"
        ordering = ['-timestamp']
        app_label = "infrastructure"

    def __str__(self):
        return f"History: {self.barber} - {self.action[:30]}"