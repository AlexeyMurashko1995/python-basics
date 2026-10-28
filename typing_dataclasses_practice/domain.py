from decimal import Decimal
from dataclasses import dataclass
from typing import Literal


@dataclass
class Transaction:
    id: str
    amount: Decimal
    currency: Literal["USD", "EUR", "PLN"]
    description: str | None = None
    status: Literal["pending", "completed", "failed"] = "pending"

    def __post_init__(self) -> None:
        if self.amount <= Decimal("0"):
            raise ValueError("Amount must be greater than zero")