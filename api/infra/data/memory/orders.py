from functools import reduce
from typing import Dict, List

from domain.entities import Order
from domain.exceptions import OrderDoesNotExists
from domain.repositories import OrdersRepository

from .data import ORDERS


def _create_beer_map(beers: List[Order]) -> Dict[str, Order]:
    return reduce(
        lambda acc, beer: {**acc, str(beer.id): beer},
        beers,
        {}
    )

# iter the list only once and then just call by direct reference provided (hashmap)
ORDERS_BY_ID: Dict[str, Order] = _create_beer_map(ORDERS)


class MemoryOrdersRepository(OrdersRepository):

    def __init__(self, initial_orders: List[Order] | None = None):
        # if the data is not specified, use the mock data
        self._orders = initial_orders or ORDERS
        self._orders_by_id = ORDERS_BY_ID if initial_orders is None else _create_beer_map(initial_orders)


    def list(self) -> List[Order]:
        return self._orders


    def retrieve_by_id(self, id: str) -> Order:
        order = self._orders_by_id.get(id)
        if order is None:
            raise OrderDoesNotExists(f'Requested order with id ”{id}” does not exists')

        return order
