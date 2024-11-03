import logging
from typing import List

from domain.entities import BeerStock
from domain.repositories import BeersStockRepository

logger = logging.getLogger(__name__)


class ListBeersStockByIdsUseCase:
    def __init__(self, beers_stock_repository: BeersStockRepository):
        self._beers_stock_repository = beers_stock_repository

    def execute(self, ids: List[str]) -> List[BeerStock]:
        results = self._beers_stock_repository.list_by_ids(ids=ids)

        logger.info("list beers stock done!", len(results))
        return results
