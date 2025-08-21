from core.application.order.services import OrderService
from core.application.order.dtos import CreateOrderDTO

def create_order(service: OrderService, user_id: int, total: float):
    dto = CreateOrderDTO(user_id=user_id, total=total)
    return service.create_order(dto)

def list_orders(service: OrderService, user_id: int):
    return service.list_orders(user_id)
