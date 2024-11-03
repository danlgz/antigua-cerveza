from datetime import datetime
from uuid import UUID

from pydantic import PositiveFloat, PositiveInt

from .base import Base


class BeerStock(Base):
    """
    A model representing the stock details of a specific beer.

    Attributes:
        id (UUID): A unique identifier for the beer stock item.
        name (str): The name of the beer.
        price (PositiveFloat): The price per unit of the beer.
        quantity (PositiveInt): The available quantity of the beer in stock.
        last_updated (date): The date when the stock was last updated.
    """

    id: UUID
    name: str
    price: PositiveFloat
    quantity: PositiveInt
    last_updated: datetime
