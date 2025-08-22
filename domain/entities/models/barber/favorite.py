from django.db import models

from config.settings.base import AUTH_USER_MODEL
from domain.entities.models.shared import BaseModel
from . import Barber



class Favorite(BaseModel):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='favorite_barbers')
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user', 'barber')
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"
        app_label = "infrastructure"

    def __str__(self):
        return f"{self.user} ❤️ {self.barber}"