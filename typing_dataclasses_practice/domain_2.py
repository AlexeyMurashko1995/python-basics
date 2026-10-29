from dataclasses import dataclass
from typing import Literal
from decimal import Decimal


@dataclass
class Transaction:
    id: str
    amount: Decimal
    currency: Literal["EUR", "USD", "PLN"]
    description: str | None = None
    status: Literal["pending", "completed", "failed"] = "pending"

    def __post_init__(self) -> None:
        if self.amount <= Decimal("0"):
            raise ValueError("Amount must be positive")

    def complete(self) -> None:
        if self.status == "completed" or self.status == "failed":
            raise ValueError("Transaction is already finalized")
        self.status = "completed"


@dataclass
class Account:
    id: str
    user_id: str
    currency: Literal["USD", "EUR", "PLN"]
    balance: Decimal = Decimal("0")