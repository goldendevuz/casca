from django.db.models.signals import post_save
from django.dispatch import receiver

from domain.entities.models.barber import Barber, History, WorkingHour, SecuritySetting

@receiver(post_save, sender=Barber)
def create_barber_related_data(sender, instance, created, **kwargs):
    if created:
        # History yaratish
        History.objects.create(
            barber=instance,
            action="Barber profile created."
        )

        # Default WorkingHour (Dushanba–Juma, 9:00–17:00)
        default_working_hours = [
            (0, "09:00", "17:00"),
            (1, "09:00", "17:00"),
            (2, "09:00", "17:00"),
            (3, "09:00", "17:00"),
            (4, "09:00", "17:00"),
        ]
        for day, start, end in default_working_hours:
            WorkingHour.objects.create(
                barber=instance,
                day_of_week=day,
                start_time=start,
                end_time=end,
            )

        # SecuritySetting yaratish
        SecuritySetting.objects.get_or_create(user=instance.user)
    else:
        # Update bo‘lsa Historyga yozamiz
        History.objects.create(
            barber=instance,
            action="Barber profile updated."
        )