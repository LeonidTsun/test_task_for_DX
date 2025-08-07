from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID

@dataclass
class Offer:
    """
    Represents a single offer for a product.
    """
    id: UUID
    price: int
    items_in_stock: int

@dataclass
class Product:
    """
    Represents a product that can have multiple offers.
    """
    id: UUID
    name: str
    description: str
    offers: Optional[List[Offer]] = None
