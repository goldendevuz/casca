# This file makes Django aware of the User model defined deeper in infrastructure.
from core.domain.entities.models.user import User

__all__ = ["User"]
