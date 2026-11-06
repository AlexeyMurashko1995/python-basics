from dataclasses import dataclass, field
from decimal import Decimal
from enum import StrEnum
from typing import Self
from uuid import uuid4, UUID


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

    def __str__(self) -> str:
        return f"{self.weight} {self.unit}"

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

    def __gt__(self, other: Self) -> bool:
        if not isinstance(other, Weight):
            return NotImplemented

        if self.unit != other.unit:
            raise ValueError("The units are different")

        return self.weight > other.weight

    def __lt__(self, other: Self) -> bool:
        if not isinstance(other, Weight):
            return NotImplemented

        if self.unit != other.unit:
            raise ValueError("The units are different")

        return self.weight < other.weight

    def __ge__(self, other: Self) -> bool:
        if not isinstance(other, Weight):
            return NotImplemented

        if self.unit != other.unit:
            raise ValueError("The units are different")

        return self.weight >= other.weight

    def __le__(self, other: Self) -> bool:
        if not isinstance(other, Weight):
            return NotImplemented

        if self.unit != other.unit:
            raise ValueError("The units are different")

        return self.weight <= other.weight


@dataclass
class Shipment:
    customer_id: int
    shipment_id: UUID = field(default_factory=uuid4)
    cargo_manifest: dict[Unit, Weight] = field(default_factory=dict)

    def add_cargo(self, weight: Weight) -> None:
        if weight.unit not in self.cargo_manifest:
            self.cargo_manifest[weight.unit] = weight
        else:
            self.cargo_manifest[weight.unit] += weight

    def remove_cargo(self, weight: Weight) -> None:
        current_weight = self.cargo_manifest.get(weight.unit)

        if current_weight is None or current_weight < weight:
            raise ValueError("Insufficient cargo weight")

        self.cargo_manifest[weight.unit] -= weight