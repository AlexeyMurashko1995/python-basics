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

    def get_total_price(self) -> Decimal:
        total_price = Decimal("0")
        for product in self.products_list:
            total_price += product.price
        return total_price

    def delete_by_product_id(self, product_id: UUID) -> Product:
        for product in self.products_list:
            if product.id == product_id:
                self.products_list.remove(product)
                return product
        raise ValueError("Product not found")

    def filter_by_category(self,  category: ProductCategory) -> list[Product]:
        target_product_list = []
        for product in self.products_list:
            if product.category == category:
                target_product_list.append(product)
        return target_product_list

    def get_expensive_product(self) -> Product | None:
        most_expensive = None
        for product in self.products_list:
            if most_expensive is None or product.price > most_expensive.price:
                most_expensive = product
        return most_expensive