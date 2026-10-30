from dataclasses import dataclass
from decimal import Decimal
from typing import Literal


@dataclass
class Invoice:
    id: str
    user_id: str
    amount: Decimal
    currency: Literal["USD", "EUR", "PLN"]
    status: Literal["draft", "issued", "paid", "cancelled"] = "draft"
    description: str | None = None

    def __post_init__(self) -> None:
        if self.amount <= Decimal("0"):
            raise ValueError("Invoice amount must be positive")

    def issue(self) -> None:
        if self.status == "draft":
            self.status = "issued"
        else:
            raise ValueError("Only draft invoices can be issued")

    def pay(self) -> None:
        if self.status != "issued":
            raise ValueError("Only issued invoices can be paid")
        self.status = "paid"