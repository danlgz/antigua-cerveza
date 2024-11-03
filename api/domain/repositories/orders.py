from typing import List, Protocol

from domain.entities import Order


class OrdersRepository(Protocol):
    def retrieve_by_id(self, id: str) -> Order: ...

    def list(self) -> List[Order]: ...
