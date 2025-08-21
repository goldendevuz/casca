from typing import Optional
from core.application.interfaces.repositories import UserRepository
from core.application.user.dtos import RegisterUserDTO
from core.domain.user.entities import UserEntity

class UserService:
    def __init__(self, users: UserRepository):
        self.users = users

    def register(self, dto: RegisterUserDTO) -> UserEntity:
        existing = self.users.get_by_email(dto.email)
        if existing:
            return existing
        return self.users.create(email=dto.email)
