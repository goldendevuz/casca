from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .. import Appointment
from config.settings.base import AUTH_USER_MODEL
from core.infrastructure.db.models.shared.base import BaseModel



class Review(BaseModel):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    recommend = models.BooleanField(default=True)

    def clean(self):
        super().clean()
        if self.text:
            if len(self.text) < 10:
                raise ValidationError({'text': 'Text is too short (min 10 characters).'})
            elif len(self.text) > 1000:
                raise ValidationError({'text': 'Text is too long (max 1000 characters).'})

    def __str__(self):
        return f"Review by {self.user} - {self.rating}⭐"