from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class OrderCreated:
    order_id: int
    user_id: int
    total: float
