from dataclasses import dataclass
from typing import Dict, List
from uuid import UUID

from domain.entities import BeerStock, OrderItem, OrderRound, OrderRoundItem
from domain.repositories import BeersStockRepository


@dataclass
class OrderSummary:
    """Represents the final summary of all beer orders"""
    items: List[OrderItem]
    total: float


class OrderRoundBeerCalculator:
    """
    Calculates totals and quantities for beer orders across multiple rounds.
    """
    def __init__(self, beer_stock_repository: BeersStockRepository):
        self._beer_stock_repository = beer_stock_repository

    def calculate_order_summary(self, rounds: List[OrderRound]) -> OrderSummary:
        """
        Calculate a summary of all beer orders across multiple rounds.

        Args:
            rounds: List of OrderRound objects containing order information

        Returns:
            OrderSummary containing the list of items and total amount
        """
        grouped_items = self._group_items_by_beer(rounds)
        beers = self._beer_stock_repository.list_by_ids(list(grouped_items.keys()))

        beer_summaries = self._calculate_beer_summaries(beers, grouped_items)
        total_amount = round(sum(summary.total for summary in beer_summaries.values()), 2)

        return OrderSummary(
            items=[OrderItem(**summary.dict()) for summary in beer_summaries.values()],
            total=total_amount
        )

    def _group_items_by_beer(self, rounds: List[OrderRound]) -> Dict[str, List[OrderRoundItem]]:
        """Group order items by beer ID."""
        grouped_items: Dict[str, List[OrderRoundItem]] = {}

        for round_order in rounds:
            for item in round_order.items:
                beer_id = str(item.beer_stock_id)
                if beer_id not in grouped_items:
                    grouped_items[beer_id] = []
                grouped_items[beer_id].append(item)

        return grouped_items

    def _calculate_beer_summaries(
        self,
        beers: List[BeerStock],
        grouped_items: Dict[str, List[OrderRoundItem]]
    ) -> Dict[str, OrderItem]:
        """Calculate summaries for each beer."""
        summaries: Dict[str, OrderItem] = {}

        for beer in beers:
            beer_id = str(beer.id)
            if beer_id not in grouped_items:
                continue

            quantity = sum(item.quantity for item in grouped_items[beer_id])
            total = round(quantity * beer.price, 2)

            summaries[beer_id] = OrderItem(
                price_per_unit=beer.price,
                total=total,
                beer_stock_id=UUID(beer_id),
                quantity=quantity
            )

        return summaries
