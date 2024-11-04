from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock
from uuid import UUID

from application.use_cases.retrieve_order import RetrieveOrderUsecase
from domain.entities import (
    BeerStock,
    Order,
    OrderItem,
    OrderRound,
    OrderRoundItem,
)
from domain.repositories import BeersStockRepository
from domain.repositories.orders import OrdersRepository

date_format = "%Y-%m-%d %H:%M:%S"

class TestListOrders(TestCase):
    def test_list_orders_successfully(self):
        beers_repo = Mock(BeersStockRepository)
        orders_repo = Mock(OrdersRepository)

        orders_repo.retrieve_by_id.return_value = Order(
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
        beers_repo.list_by_ids.return_value = [
            BeerStock(
                id=UUID("4bfda8eb-3531-4efa-ab19-bf41f8482f14"),
                name="Muy Noble",
                price=5.18,
                last_updated=datetime.strptime("2024-10-03 15:30:00", "%Y-%m-%d %H:%M:%S"),
                quantity=100,
                img="/",
            )
        ]

        use_case = RetrieveOrderUsecase(beers_stock_repository=beers_repo, orders_repository=orders_repo)
        result = use_case.execute(id="96413732-3142-47c4-ad78-e99fec8a5492")

        orders_repo.retrieve_by_id.assert_called_once()
        beers_repo.list_by_ids.assert_called_once()
        self.assertEqual(result, Order(
                id=UUID("96413732-3142-47c4-ad78-e99fec8a5492"),
                discounts=4.0,
                # the `items` are calculated by "order round beer calculator" service, this part of the test is so import!
                items=[
                    OrderItem(
                        beer_stock_id=UUID("4bfda8eb-3531-4efa-ab19-bf41f8482f14"),
                        price_per_unit=5.18,
                        quantity=3,
                        total=15.54,
                    )
                ],
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
                subtotal=15.54,
                taxes=4.0,
                total=15.54, # calculaded: subtotal + taxes - discounts
            )
        )
