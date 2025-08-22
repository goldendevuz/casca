from django.db import models

from domain.entities.models.shared.base import BaseModel

class Reason(BaseModel):
    class RescheduleReason(models.TextChoices):
        CLASH = "clash", "Schedule clash"
        NOT_AVAILABLE = "not_available", "Not available"
        IMPORTANT_ACTIVITY = "important_activity", "Important activity"
        NO_COMMENT = "no_comment", "No comment"
        OTHER = "other", "Other"

    class CancelReason(models.TextChoices):
        CHANGE_BARBER = "change_barber", "Change barber"
        CHANGE_PACKAGE = "change_package", "Change package"
        NO_CONSULT = "no_consult", "No consult needed"
        RECOVERED = "recovered", "Recovered"
        FOUND_MEDICINE = "found_medicine", "Found medicine"
        JUST_CANCEL = "just_cancel", "Just cancel"
        NO_COMMENT = "no_comment", "No comment"
        OTHER = "other", "Other"

    reschedule = models.CharField(
        max_length=50,
        choices=RescheduleReason.choices,
        null=True,
        blank=True
    )
    cancel = models.CharField(
        max_length=50,
        choices=CancelReason.choices,
        null=True,
        blank=True
    )
    other = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Reschedule: {self.get_reschedule_display() or '-'}, Cancel: {self.get_cancel_display() or '-'}"