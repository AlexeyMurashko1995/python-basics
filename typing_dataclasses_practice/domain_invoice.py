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

    def cancel(self, reason: str | None = None) -> None:
        if self.status == "paid":
            raise ValueError("Paid invoice cannot be cancelled")
        elif self.status == "cancelled":
            raise ValueError("Invoice is already cancelled")
        self.status = "cancelled"
        if reason is not None:
            if self.description is None:
                self.description = f"Cancelled: {reason}"
            else:
                self.description = self.description + f" | Cancelled: {reason}"

    def apply_discount(self, discount_amount: Decimal) -> None:
        if self.status != "draft":
            raise ValueError("Discount can only be applied to draft invoices")
        if discount_amount <= Decimal("0"):
            raise ValueError("Discount amount must be positive")
        elif discount_amount >= self.amount:
            raise ValueError("Discount cannot exceed or equal invoice amount")
        self.amount -= discount_amount