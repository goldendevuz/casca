from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string

from core.infrastructure.db.models.user.user import NEW, PATIENT, VIA_PHONE, User

class Command(BaseCommand):
    help = 'Generate 100 test users'

    def handle(self, *args, **options):
        count = 0
        for i in range(100):
            phone = f'+99890{get_random_string(7, allowed_chars="0123456789")}'
            username = f'testuser{i}'
            email = f'{username}@example.com'

            # Agar phone yoki email allaqachon mavjud bo‘lsa — o'tkazib yuboramiz
            if User.objects.filter(username=username).exists():
                continue

            User.objects.create_user(
                username=username,
                phone=phone,
                email=email,
                password='test1234',  # test parol
                role=PATIENT,
                auth_type=VIA_PHONE,
                auth_status=NEW,
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(f"✅ {count} ta test foydalanuvchi yaratildi."))
