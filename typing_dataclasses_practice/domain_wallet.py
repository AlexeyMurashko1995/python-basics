from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum


class Currency(StrEnum):
    USD = "USD"
    EUR = "EUR"
    PLN = "PLN"


@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: Currency

    def __post_init__(self) -> None:
        if self.amount < Decimal("0"):
            raise ValueError("Money amount cannot be negative")

    def add(self, other: Money) -> Money:
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        new_obj = Money(self.amount + other.amount, currency=self.currency)
        return new_obj