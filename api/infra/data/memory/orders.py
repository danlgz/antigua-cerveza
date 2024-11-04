from functools import reduce
from typing import Dict, List

from domain.entities import Order
from domain.exceptions import OrderDoesNotExists
from domain.repositories import OrdersRepository

from .data import ORDERS

# iter the list only once and then just call by direct reference provided (hashmap)
ORDERS_BY_ID: Dict[str, Order] = reduce(lambda acc, order: {str(order.id): order, **acc}, ORDERS, {})


class MemoryOrdersRepository(OrdersRepository):

    def list(self) -> List[Order]:
        return ORDERS


    def retrieve_by_id(self, id: str) -> Order:
        order = ORDERS_BY_ID.get(id)
        if order is None:
            raise OrderDoesNotExists(f'Requested order with id ”{id}” does not exists')

        return order
