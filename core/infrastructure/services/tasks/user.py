from celery import shared_task
from core.domain.entities.models.user import User

@shared_task
def process_user_photo(user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return f"User {user_id} not found"

    print(f"🖼️ Processing photo for user: {user.email or user.username}")
    # Simulyatsiya: rasmni tahlil qilish, siqish yoki boshqa narsa
    return f"Photo processed for user {user_id}"
