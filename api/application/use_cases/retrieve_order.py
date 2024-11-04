from application.services import OrderRoundBeerCalculator
from domain.entities import Order
from domain.repositories import BeersStockRepository, OrdersRepository


class RetrieveOrderUsecase:
    def __init__(self, orders_repository: OrdersRepository, beers_stock_repository: BeersStockRepository):
        self._orders_repository = orders_repository
        self._order_round_beer_calculator = OrderRoundBeerCalculator(beer_stock_repository=beers_stock_repository)


    def execute(self, id: str):
        order = self._orders_repository.retrieve_by_id(id)

        summary = self._order_round_beer_calculator.calculate_order_summary(order.rounds)
        subtotal = summary.total

        return Order(
            **order.dict(exclude={"items", "subtotal", "total"}),
            items=summary.items,
            subtotal=subtotal,
            total=round(subtotal - order.taxes - order.discounts, 2),
        )
