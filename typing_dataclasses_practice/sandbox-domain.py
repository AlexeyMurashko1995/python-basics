from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum
from typing import Self


class Unit(StrEnum):
    KG = "KG"
    LB = "LB"
    TON = "TON"


@dataclass(frozen=True)
class Weight:
    weight: Decimal
    unit: Unit

    def __post_init__(self) -> None:
        if self.weight <= Decimal("0"):
            raise ValueError("Weight must be positive")

    def __add__(self, other: Self) -> Self:
        if not isinstance(other, Weight):
            return NotImplemented

        if self.unit != other.unit:
            raise ValueError("The units are different")

        return Weight(self.weight + other.weight, self.unit)

    def __sub__(self, other: Self) -> Self:
        if not isinstance(other, Weight):
            return NotImplemented

        if self.unit != other.unit:
            raise ValueError("The units are different")

        return Weight(self.weight - other.weight, self.unit)