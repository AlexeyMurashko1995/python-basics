from dataclasses import dataclass
from decimal import Decimal
from enum import StrEnum


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