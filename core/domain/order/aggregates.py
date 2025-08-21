from dataclasses import dataclass
from .entities import OrderEntity

@dataclass(slots=True)
class OrderAggregate:
    order: OrderEntity
