from dataclasses import dataclass, field
from decimal import Decimal
from enum import StrEnum
from uuid import UUID, uuid4



class CargoCategory(StrEnum):
    ELECTRONICS = "ELECTRONICS"
    CLOTHING = "CLOTHING"
    FOOD = "FOOD"


@dataclass(frozen=True)
class CargoBox:
    weight: Decimal
    category: CargoCategory
    is_fragile: bool
    box_id: UUID = field(default_factory=uuid4)

    def __post_init__(self) -> None:
        if self.weight <= Decimal("0"):
            raise ValueError("Weight amount must be positive")

    def get_info(self) -> str:
        return f"CargoBox {self.box_id}: category={self.category}, weight={self.weight} kg"


@dataclass
class Shipment:
    boxes: list[CargoBox] = field(default_factory=list)
    shipment_id: UUID = field(default_factory=uuid4)

    def add_box(self, box: CargoBox) -> None:
        self.boxes.append(box)

    def get_total_weight(self) -> Decimal:
        total_weight = Decimal("0")
        for box in self.boxes:
            total_weight += box.weight
        return total_weight