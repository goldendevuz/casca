from dataclasses import dataclass
from .entities import UserEntity

@dataclass(slots=True)
class UserAggregate:
    user: UserEntity
