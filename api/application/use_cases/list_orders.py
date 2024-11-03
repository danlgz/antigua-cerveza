from domain.repositories import OrdersRepository


class ListOrdersUsecase:
    def __init__(self, orders_repository: OrdersRepository):
        self._orders_repository = orders_repository


    def execute(self):
        return self._orders_repository.list()
