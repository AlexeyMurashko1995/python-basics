from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum
from typing import Self


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

    def __add__(self, other: Self) -> Self:
        if self.currency != other.currency:
            raise ValueError("Two different currencies")
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other: Self) -> Self:
        if self.currency != other.currency:
            raise ValueError("Two different currencies")
        return Money(self.amount - other.amount, self.currency)