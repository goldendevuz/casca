from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from config.settings.base import AUTH_USER_MODEL
from domain.entities.models.shared import BaseModel
from .review import Review


class Rate(BaseModel):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='rates')
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user} rated {self.value}⭐"
