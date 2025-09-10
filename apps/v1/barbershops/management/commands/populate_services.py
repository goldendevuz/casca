from django.core.management.base import BaseCommand

from apps.v1.barbershops.models import Service


class Command(BaseCommand):
    help = "Populate default services"

    SERVICES = [
        "Hair Cut",
        "Hair Coloring",
        "Hair Wash",
        "Shaving",
        "Skin Care",
        "Hair Dryer",
        "Face Make up",
    ]

    def handle(self, *args, **options):
        for service_name in self.SERVICES:
            service, created = Service.objects.get_or_create(
                translations__name=service_name
            )
            if created:
                service.set_current_language("en")
                service.name = service_name
                service.save()
                self.stdout.write(self.style.SUCCESS(f"Created service: {service_name}"))
            else:
                self.stdout.write(f"Service already exists: {service_name}")
