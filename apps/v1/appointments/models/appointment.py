from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.v1.shared.models import BaseModel


class SeatCount(models.TextChoices):
    ONE_SEAT = "one_seat", _("One Seat")
    TWO_SEATS = "two_seats", _("Two Seats")
    MULTIPLE = "multiple", _("Multiple Seats")


class Appointment(BaseModel):
    customer = models.ForeignKey(
        "accounts.Profile",
        on_delete=models.CASCADE,
        related_name="appointments",
        verbose_name=_("Customer"),
        help_text=_("The profile of the customer"),
    )
    barber = models.ForeignKey(
        "barbershops.Barber",
        on_delete=models.CASCADE,
        related_name="appointments",
        verbose_name=_("Barber"),
        help_text=_("The barber assigned to the appointment"),
    )
    seat_count = models.CharField(
        verbose_name=_("Seat Count"),
        max_length=20,
        choices=SeatCount.choices,
        default=SeatCount.ONE_SEAT,
        help_text=_("The number of seats reserved for the appointment"),
    )
    payment = models.ForeignKey(
        "payments.Payment",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="appointments",
        verbose_name=_("Payment"),
        help_text=_("The payment associated with the appointment"),
    )
    promotion = models.ForeignKey(
        "promotions.Promotion",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="appointments",
        verbose_name=_("Promotion"),
        help_text=_("The promotion applied to the appointment"),
    )
    total_price = models.IntegerField(
        verbose_name=_("Total Price"),
        help_text=_("The total price of the appointment"),
    )
    status = models.CharField(
        verbose_name=_("Status"),
        max_length=20,
        choices=AppointmentStatuses.choices,
        default=AppointmentStatuses.PENDING,
        help_text=_("The status of the appointment"),
    )
    mood_during_appointment = models.ForeignKey(
        "moods.Mood",
        on_delete=models.CASCADE,
        related_name="appointments",
        verbose_name=_("Mood During Appointment"),
        help_text=_("The mood recorded during the appointment"),
    )
    date = models.DateField(
        verbose_name=_("Date"),
        help_text=_("The date of the appointment"),
    )
    time = models.TimeField(
        verbose_name=_("Time"),
        help_text=_("The time of the appointment"),
    )
    barbershop = models.ForeignKey(
        "barbershops.Barbershop",
        on_delete=models.CASCADE,
        related_name="appointments",
        verbose_name=_("Barbershop"),
        help_text=_("The barbershop for the appointment"),
    )
    remind_me = models.BooleanField(
        verbose_name=_("Remind Me"),
        default=True,
        help_text=_("Whether to remind the customer about the appointment"),
    )

    class Meta:
        ordering = ["-date", "-time"]
        verbose_name = _("Appointment")
        verbose_name_plural = _("Appointments")

    def __str__(self):
        return f"{self.customer} with {self.barber} at {self.barbershop} on {self.date} {self.time}"
