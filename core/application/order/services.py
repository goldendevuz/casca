from core.application.interfaces.repositories import OrderRepository
from core.application.order.dtos import CreateOrderDTO
from core.domain.order.entities import OrderEntity

class OrderService:
    def __init__(self, orders: OrderRepository):
        self.orders = orders

    def create_order(self, dto: CreateOrderDTO) -> OrderEntity:
        return self.orders.create(user_id=dto.user_id, total=dto.total)

    def list_orders(self, user_id: int):
        return list(self.orders.list_by_user(user_id))
