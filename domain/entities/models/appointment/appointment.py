from datetime import datetime

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.timezone import make_aware

from config.settings.base import AUTH_USER_MODEL
from .reason import Reason
from ..barber import Barber
from ..barbershop import Service
from ..shared import BaseModel


class Appointment(BaseModel):
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        APPROVED = 'approved', 'Approved'
        CANCELED = 'canceled', 'Canceled'
        COMPLETED = 'completed', 'Completed'
        RESCHEDULED = 'rescheduled', 'Rescheduled'

    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='appointments')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    age = models.PositiveIntegerField()
    problem = models.TextField(blank=True)
    reason = models.ForeignKey(Reason, on_delete=models.SET_NULL, null=True, related_name='appointments')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)

    @property
    def appointment_time(self):
        if self.date and self.time:
            return datetime.combine(self.date, self.time)
        return None

    def clean(self):
        super().clean()
        if self.date and self.time:
            combined_datetime = datetime.combine(self.date, self.time)

            # Convert to timezone-aware datetime if it's naive
            if timezone.is_naive(combined_datetime):
                combined_datetime = make_aware(combined_datetime)

            if combined_datetime < timezone.now():
                raise ValidationError({'date': 'Appointment date and time cannot be in the past.'})

    def __str__(self):
        return f"{self.full_name} with Dr. {self.barber.user.get_full_name()} on {self.date} at {self.time}"
