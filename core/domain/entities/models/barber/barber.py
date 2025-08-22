from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from config.settings.base import AUTH_USER_MODEL
from core.domain.entities.models.shared import BaseModel
from core.domain.entities.models.barbershop import Barbershop, Specialty

class Barber(BaseModel):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='barber_profile')
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True, related_name='barber')
    barbershop = models.ForeignKey(Barbershop, on_delete=models.SET_NULL, null=True, related_name='barber')
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        default=0.0,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)
        ]
    )
    review_count = models.PositiveIntegerField(default=0)
    about = models.TextField(blank=True)

    def __str__(self):
        # Agar user full name bo'lmasa, username ko'rsatiladi
        full_name = self.user.get_full_name()
        if not full_name.strip():
            full_name = self.user.username
        return f"Dr. {full_name}"