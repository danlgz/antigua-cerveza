from datetime import date
from typing import List
from uuid import UUID

from pydantic import PositiveFloat
from pydantic.types import PositiveInt

from .base import Base


class OrderItem(Base):
    """
    Represents a single item within an order, detailing pricing and identification of a beer stock item.

    Attributes:
        beer_stock_id (UUID): Unique identifier for the beer stock item.
        price_per_unit (PositiveFloat): Price of each unit of the beer.
        total (PositiveFloat): Total cost for this item, calculated as quantity multiplied by price per unit.
    """
    beer_stock_id: UUID
    price_per_unit: PositiveFloat
    total: PositiveFloat


class OrderRoundItem(Base):
    """
    Specifies an item in an order round, including the quantity of a specific beer.

    Attributes:
        beer_stock_id (UUID): Unique identifier for the beer stock item.
        quantity (PositiveInt): Quantity of the beer ordered in this round.
    """
    beer_stock_id: UUID
    quantity: PositiveInt


class OrderRound(Base):
    """
    Represents a specific round within an order, including the items ordered and the creation date.

    Attributes:
        created (date): Date when the round was created.
        items (List[OrderRoundItem]): List of items in this round of the order.
    """
    created: date
    items: List[OrderRoundItem]


class Order(Base):
    """
    Represents a complete order with payment status, cost details, and individual rounds.

    Attributes:
        paid (bool): Payment status of the order.
        total (PositiveFloat): Final total of the order after taxes and discounts.
        subtotal (PositiveFloat): Initial subtotal before any taxes and discounts.
        taxes (PositiveFloat): Total tax amount applied to the order.
        discounts (PositiveFloat): Total discounts applied to the order.
        items (List[OrderItem]): List of items included in the order.
        rounds (List[OrderRound]): List of rounds, each containing items ordered in separate batches.
    """
    paid: bool
    total: PositiveFloat
    subtotal: PositiveFloat
    taxes: PositiveFloat
    discounts: PositiveFloat
    items: List[OrderItem]
    rounds: List[OrderRound]
