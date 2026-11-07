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

    def __post_init__(self) -> None:
        if self.price <= Decimal("0"):
            raise ValueError("Product price must be positive")

    def product_data(self) -> str:
        return f"Product id: {self.id}; category: {self.category}; price: {self.price}"


@dataclass
class Inventory:
    products_list: list[Product] = field(default_factory=list)

    def add_product(self, product: Product) -> Product:
        if product is not None:
            self.products_list.append(product)
            return product