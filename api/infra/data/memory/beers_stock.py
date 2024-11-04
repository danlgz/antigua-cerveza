from functools import reduce
from typing import Dict, List

from domain.entities import BeerStock
from domain.exceptions import BeerStockDoesNotExists
from domain.repositories import BeersStockRepository

from .data import BEERS_STOCK


def _create_beer_map(beers: List[BeerStock]) -> Dict[str, BeerStock]:
    return reduce(
        lambda acc, beer: {**acc, str(beer.id): beer},
        beers,
        {}
    )


# iter the list only once and then just call by direct reference provided (hashmap)
BEERS_STOCK_BY_ID: Dict[str, BeerStock] = _create_beer_map(BEERS_STOCK)


class MemoryBeersStockRepository(BeersStockRepository):

    def __init__(self, initial_beers: List[BeerStock] | None = None):
        # if the data is not specified, use the mock data
        self._beers = initial_beers or BEERS_STOCK
        self._beers_by_id = BEERS_STOCK_BY_ID if initial_beers is None else _create_beer_map(self._beers)


    def list_by_ids(self, ids: List[str]) -> List[BeerStock]:
        # if the id is not specifiy return all elements
        if len(ids) == 0:
            return self._beers

        # return the requested records excluding the non-existend (None)
        return [self._beers_by_id[id] for id in ids if id in self._beers_by_id]


    def retrieve_by_id(self, id: str) -> BeerStock:
        beer = self._beers_by_id.get(id)
        if beer is None:
            raise BeerStockDoesNotExists(f'Requested beer stock with id ”{id}” does not exists')

        return beer
