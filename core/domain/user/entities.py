from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True, slots=True)
class UserEntity:
    id: Optional[int]
    email: str
    is_active: bool = True
