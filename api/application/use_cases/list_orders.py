from application.services import OrderRoundBeerCalculator
from domain.entities import Order
from domain.repositories import BeersStockRepository, OrdersRepository


class ListOrdersUsecase:
    def __init__(self, orders_repository: OrdersRepository, beers_stock_repository: BeersStockRepository):
        self._orders_repository = orders_repository
        self._order_round_beer_calculator = OrderRoundBeerCalculator(beer_stock_repository=beers_stock_repository)


    def execute(self):
        orders = []

        for order in self._orders_repository.list():
            group = self._order_round_beer_calculator.calculate_order_summary(order.rounds)
            subtotal = group.total

            orders.append(
                Order(
                    **order.dict(exclude={"items", "subtotal", "total"}),
                    items=group.items,
                    subtotal=subtotal,
                    total=round(subtotal - order.taxes - order.discounts, 2),
                )
            )

        return orders
