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

    def __post_init__(self) -> None:
        if self.balance < Decimal("0"):
            raise ValueError("Initial balance cannot be negative")

    def deposit(self, amount: Decimal) -> None:
        if amount <= Decimal("0"):
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount: Decimal) -> None:
        if amount <= Decimal("0"):
            raise ValueError("Withdraw must be positive")
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount