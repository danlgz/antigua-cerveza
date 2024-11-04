from functools import reduce
from typing import Dict, List

from domain.entities import BeerStock
from domain.repositories import BeersStockRepository

from .data import BEERS_STOCK

# iter the list only once and then just call by direct reference provided (hashmap)
BEERS_STOCK_BY_ID: Dict[str, BeerStock] = reduce(lambda acc, beer: {str(beer.id): beer, **acc}, BEERS_STOCK, {})


class MemoryBeersStockRepository(BeersStockRepository):

    def list_by_ids(self, ids: List[str]) -> List[BeerStock]:
        # if the id is not specifiy return all elements
        if len(ids) == 0:
            return BEERS_STOCK

        # return the requested records excluding the non-existend (None)
        return [BEERS_STOCK_BY_ID[id] for id in ids if id in BEERS_STOCK_BY_ID]


    def retrieve_by_id(self, id: str) -> BeerStock:
        beer = BEERS_STOCK_BY_ID.get(id)
        if beer is None:
            raise Exception('Beer stock not found')

        return beer
