from typing import List, Protocol

from domain.entities import BeerStock


class BeersStockRepository(Protocol):
    def retrieve_by_id(self, id: str) -> BeerStock: ...

    def list_by_ids(self, ids: List[str]) -> List[BeerStock]: ...
