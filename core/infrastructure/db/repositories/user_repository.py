from typing import Optional
from core.application.interfaces.repositories import UserRepository
from core.domain.user.entities import UserEntity
from core.infrastructure.db.models.user_models import CustomUser

class DjangoUserRepository(UserRepository):
    def get_by_id(self, user_id: int) -> Optional[UserEntity]:
        try:
            u = CustomUser.objects.get(pk=user_id)
            return UserEntity(id=u.id, email=u.email, is_active=u.is_active)
        except CustomUser.DoesNotExist:
            return None

    def get_by_email(self, email: str) -> Optional[UserEntity]:
        try:
            u = CustomUser.objects.get(email=email)
            return UserEntity(id=u.id, email=u.email, is_active=u.is_active)
        except CustomUser.DoesNotExist:
            return None

    def create(self, email: str) -> UserEntity:
        # Minimal creation without full auth flow
        u = CustomUser.objects.create_user(username=email.split("@")[0], email=email, password=None)
        return UserEntity(id=u.id, email=u.email, is_active=u.is_active)
