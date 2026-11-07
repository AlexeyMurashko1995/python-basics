from dataclasses import dataclass, field
from decimal import Decimal
from enum import StrEnum
from uuid import UUID, uuid4


class ProductCategory(StrEnum):
    TECH = "TECH"
    FURNITURE = "FURNITURE"
    BOOKS = "BOOKS"


@dataclass(frozen=True)
class Product:
    price: Decimal
    category: ProductCategory
    is_available: bool
    id: UUID = field(default_factory=uuid4)