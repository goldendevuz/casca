from dataclasses import dataclass

@dataclass(slots=True)
class CreateOrderDTO:
    user_id: int
    total: float
