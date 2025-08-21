# This file makes Django aware of the CustomUser model defined deeper in infrastructure.
from core.infrastructure.db.models import User

__all__ = ["User"]
