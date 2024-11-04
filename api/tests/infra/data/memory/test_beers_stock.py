

from datetime import datetime
from unittest.case import TestCase
from uuid import UUID

from domain.entities.beer_stock import BeerStock
from domain.exceptions import BeerStockDoesNotExists
from infra.data.memory.beers_stock import MemoryBeersStockRepository

date_format = "%Y-%m-%d %H:%M:%S"


class TestMemoryBeersStockRepository(TestCase):

    def setUp(self):
        self.mock_beers = [
            BeerStock(
                id=UUID("6aa57346-1357-47b0-923e-7a416427afae"),
                name="Sin Novia",
                price=5.18,
                last_updated=datetime.strptime("2024-10-03 15:30:00", date_format),
                quantity=100,
                img="/",
            ),
        ]
        self.repository = MemoryBeersStockRepository(self.mock_beers)


    def test_list_all_beers_by_empty_param(self):
        result = self.repository.list_by_ids(ids=[])

        self.assertEqual(result, [
            BeerStock(
                id=UUID("6aa57346-1357-47b0-923e-7a416427afae"),
                name="Sin Novia",
                price=5.18,
                last_updated=datetime.strptime("2024-10-03 15:30:00", date_format),
                quantity=100,
                img="/",
            ),
        ])

    def test_list_empty_beers_by_not_found_id(self):
        result = self.repository.list_by_ids(ids=["caa57346-1357-47b0-923e-7a416427afac"])

        self.assertEqual(result, [])


    def test_list_beers_by_given_id(self):
        result = self.repository.list_by_ids(ids=["6aa57346-1357-47b0-923e-7a416427afae"])

        self.assertEqual(result, [
            BeerStock(
                id=UUID("6aa57346-1357-47b0-923e-7a416427afae"),
                name="Sin Novia",
                price=5.18,
                last_updated=datetime.strptime("2024-10-03 15:30:00", date_format),
                quantity=100,
                img="/",
            ),
        ])

    def test_retirieve_beer_stock(self):
        result = self.repository.retrieve_by_id(id="6aa57346-1357-47b0-923e-7a416427afae")

        self.assertEqual(result, BeerStock(
                id=UUID("6aa57346-1357-47b0-923e-7a416427afae"),
                name="Sin Novia",
                price=5.18,
                last_updated=datetime.strptime("2024-10-03 15:30:00", date_format),
                quantity=100,
                img="/",
            )
        )


    def test_try_to_retrieve_beer_stock_and_it_does_not_exist(self):
        with self.assertRaises(BeerStockDoesNotExists):
            self.repository.retrieve_by_id(id="caa57346-1357-47b0-923e-7a416427afac")
