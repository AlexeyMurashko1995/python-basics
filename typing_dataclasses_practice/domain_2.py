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

    def __post_init__(self) -> None:
        if self.balance < Decimal("0"):
            raise ValueError("Initial balance cannot be negative")

    def deposit(self, amount: Decimal) -> None:
        if amount <= Decimal("0"):
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: Decimal) -> None:
        if amount <= Decimal("0"):
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


@dataclass
class Transfer:
    id: str
    from_account_id: str
    to_account_id: str
    amount: Decimal
    currency: Literal["USD", "EUR", "PLN"]
    status: Literal["pending", "completed", "failed"] = "pending"
    description: str | None = None

    def __post_init__(self) -> None:
        if self.amount <= Decimal("0"):
            raise ValueError("Transfer amount must be positive")
        if self.from_account_id == self.to_account_id:
            raise ValueError("Cannot transfer to the same account")

    def complete(self) -> None:
        if self.status == "completed" or self.status == "failed":
            raise ValueError("Transfer is already finalized")
        self.status = "completed"