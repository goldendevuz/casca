from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class Money:
    amount: float
    currency: str = "USD"
