from datetime import datetime
from unittest import TestCase
from uuid import UUID

from domain.entities import Order, OrderRound, OrderRoundItem
from domain.exceptions import OrderDoesNotExists
from infra.data.memory.orders import MemoryOrdersRepository

date_format = "%Y-%m-%d %H:%M:%S"

class TestMemoryOrdersRepository(TestCase):
    def setUp(self):
        self.mock_orders = [
            Order(
                id=UUID("f008d7af-3c95-46ef-b29f-72c9f6040d7e"),
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
        self.repository = MemoryOrdersRepository(self.mock_orders)


    def test_list_orders_successfully(self):
        result = self.repository.list()

        self.assertEqual(result, [
            Order(
                id=UUID("f008d7af-3c95-46ef-b29f-72c9f6040d7e"),
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
        ])


    def test_retrieve_order_by_id_successfully(self):
        order = self.repository.retrieve_by_id("f008d7af-3c95-46ef-b29f-72c9f6040d7e")

        self.assertEqual(order, Order(
            id=UUID("f008d7af-3c95-46ef-b29f-72c9f6040d7e"),
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
        ))


    def test_try_to_retrieve_order_and_it_does_not_exist(self):
        with self.assertRaises(OrderDoesNotExists):
            self.repository.retrieve_by_id("c008d7af-3c95-46ef-b29f-72c9f6040d7c")
