from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock
from uuid import UUID

from application.use_cases.list_beers_stock_by_ids import (
    ListBeersStockByIdsUseCase,
)
from domain.entities import BeerStock
from domain.repositories import BeersStockRepository


class TestListBeersStockByIdsUseCase(TestCase):
    def test_list_beers_stock_successfully(self):
        repo = Mock(BeersStockRepository)
        mock = [
            BeerStock(
                id=UUID("4bfda8eb-3531-4efa-ab19-bf41f8482f14"),
                name="Muy Noble",
                price=5.18,
                last_updated=datetime.strptime("2024-10-03 15:30:00", "%Y-%m-%d %H:%M:%S"),
                quantity=100,
                img="/",
            )
        ]
        repo.list_by_ids.return_value = mock

        use_case = ListBeersStockByIdsUseCase(beers_stock_repository=repo)
        result = use_case.execute(ids=["4bfda8eb-3531-4efa-ab19-bf41f8482f14"])

        self.assertEqual(result, mock)
