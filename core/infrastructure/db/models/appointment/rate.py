from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from config.settings.base import AUTH_USER_MODEL
from .. import Review
from core.infrastructure.db.models.shared.base import BaseModel



class Rate(BaseModel):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ratings')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='rates')
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.user} rated {self.value}⭐"