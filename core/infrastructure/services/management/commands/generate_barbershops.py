from django.core.management.base import BaseCommand

from apps.v1.barbershop.models import Barbershop

class Command(BaseCommand):
    help = 'Generate 1000 identical barbershop entries for testing'

    def handle(self, *args, **kwargs):
        barbershops = []
        for i in range(1000):
            barbershops.append(
                Barbershop(
                    name="Test barbershop",
                    address="123 Test Street, Test City",
                    phone="+998901234567",
                    email="test@example.com",
                    website="https://testbarbershop.uz",
                )
            )

        Barbershop.objects.bulk_create(barbershops)
        self.stdout.write(self.style.SUCCESS("✅ 1000 ta barbershop muvaffaqiyatli yaratildi."))