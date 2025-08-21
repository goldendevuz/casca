from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True, slots=True)
class OrderEntity:
    id: Optional[int]
    user_id: int
    total: float
    status: str = "draft"
