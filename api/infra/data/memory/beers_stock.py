from datetime import datetime
from functools import reduce
from typing import List
from uuid import UUID

from domain.entities import BeerStock
from domain.repositories import BeersStockRepository
from typing_extensions import Dict

date_format = "%Y-%m-%d %H:%M:%S"
BEERS_STOCK = [
    BeerStock(
        id=UUID("6aa57346-1357-47b0-923e-7a416427afae"),
        name="Sin Novia",
        price=5.18,
        last_updated=datetime.strptime("2024-10-03 15:30:00", date_format),
        quantity=100,
    ),
    BeerStock(
        id=UUID("152b6a83-2069-4cd8-a67e-9eb70dfc444b"),
        name="Cucurucho",
        price=5.18,
        last_updated=datetime.strptime("2024-10-03 15:30:00", date_format),
        quantity=100,
    ),
    BeerStock(
        id=UUID("4bfda8eb-3531-4efa-ab19-bf41f8482f14"),
        name="Muy Noble",
        price=5.18,
        last_updated=datetime.strptime("2024-10-03 15:30:00", date_format),
        quantity=100,
    ),
    BeerStock(
        id=UUID("4cc1aad9-6800-4161-a7d5-83564cfad766"),
        name="Panza Verde",
        price=5.18,
        last_updated=datetime.strptime("2024-10-03 15:30:00", date_format),
        quantity=100,
    )
]

# iter the list only once and then just call by direct reference provided (hashmap)
BEERS_STOCK_BY_ID: Dict[str, BeerStock] = reduce(lambda acc, beer: {acc[beer.id]: beer, **acc}, BEERS_STOCK, {})


class MemoryBeersStockRepository(BeersStockRepository):

    def list_by_ids(self, ids: List[str]) -> List[BeerStock]:
        # return the requested records excluding the non-existend (None)
        return [BEERS_STOCK_BY_ID[id] for id in ids if id in BEERS_STOCK_BY_ID]


    def retrieve_by_id(self, id: str) -> BeerStock:
        beer = BEERS_STOCK_BY_ID.get(id)
        if beer is None:
            raise Exception('Beer stock not found')

        return beer
