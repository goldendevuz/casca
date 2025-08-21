from typing import Iterable
from core.application.interfaces.repositories import OrderRepository
from core.domain.order.entities import OrderEntity
from core.infrastructure.db.models.order_models import Order

class DjangoOrderRepository(OrderRepository):
    def create(self, user_id: int, total: float) -> OrderEntity:
        o = Order.objects.create(user_id=user_id, total=total)
        return OrderEntity(id=o.id, user_id=o.user_id, total=float(o.total), status=o.status)

    def list_by_user(self, user_id: int) -> Iterable[OrderEntity]:
        for o in Order.objects.filter(user_id=user_id).order_by("-id"):
            yield OrderEntity(id=o.id, user_id=o.user_id, total=float(o.total), status=o.status)
