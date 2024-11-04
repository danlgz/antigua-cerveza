from datetime import datetime
from functools import reduce
from typing import Dict, List
from uuid import UUID

from domain.entities import Order, OrderRound, OrderRoundItem
from domain.repositories import OrdersRepository

date_format = "%Y-%m-%d %H:%M:%S"
ORDERS = [
    Order(
        id=UUID("96413732-3142-47c4-ad78-e99fec8a5492"),
        discounts=4.0,
        items=[],
        paid=False,
        rounds=[
            OrderRound(
                created=datetime.strptime("2024-10-03 15:30:00", date_format),
                items=[
                    OrderRoundItem(
                        beer_stock_id=UUID("6aa57346-1357-47b0-923e-7a416427afae"),
                        quantity=2
                    )
                ]
            ),
            OrderRound(
                created=datetime.strptime("2024-10-03 15:50:00", date_format),
                items=[
                    OrderRoundItem(
                        beer_stock_id=UUID("152b6a83-2069-4cd8-a67e-9eb70dfc444b"),
                        quantity=1
                    ),
                    OrderRoundItem(
                        beer_stock_id=UUID("4cc1aad9-6800-4161-a7d5-83564cfad766"),
                        quantity=3
                    ),
                    OrderRoundItem(
                        beer_stock_id=UUID("6aa57346-1357-47b0-923e-7a416427afae"),
                        quantity=1
                    )
                ]
            )
        ],
        subtotal=0, # calculated from rounds
        taxes=10, # this should be calculated based on some tax country criteria, in this example will be hardcoded
        total=0, # calculaded from subtotal, taxes and discounts
    ),
    Order(
        id=UUID("96413732-3142-47c4-ad78-e99fec8a5492"),
        discounts=4.0,
        items=[],
        paid=False,
        rounds=[
            OrderRound(
                created=datetime.strptime("2024-10-03 15:50:00", date_format),
                items=[
                    OrderRoundItem(
                        beer_stock_id=UUID("4bfda8eb-3531-4efa-ab19-bf41f8482f14"),
                        quantity=3
                    ),
                ]
            )
        ],
        subtotal=0,
        taxes=4.0,
        total=0,
    )
]

# iter the list only once and then just call by direct reference provided (hashmap)
ORDERS_BY_ID: Dict[str, Order] = reduce(lambda acc, order: {str(order.id): order, **acc}, ORDERS, {})


class MemoryOrdersRepository(OrdersRepository):

    def list(self) -> List[Order]:
        return ORDERS


    def retrieve_by_id(self, id: str) -> Order:
        order = ORDERS_BY_ID.get(id)
        if order is None:
            raise Exception('Order not found')

        return order
