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