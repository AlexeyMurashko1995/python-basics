from decimal import Decimal
from enum import StrEnum
from pydantic import BaseModel, Field, field_validator
from uuid import UUID, uuid4


class Currency(StrEnum):
    USD = "USD"
    EUR = "EUR"
    PLN = "PLN"


class PaymentStatus(StrEnum):
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class Payment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    amount: Decimal = Field(gt=Decimal("0"))
    currency: Currency
    description: str | None = Field(default=None, max_length=100)

    @field_validator("description")
    @classmethod
    def check_description(cls, v: str | None) -> str | None:
        if v is not None:
            if v.strip() == "":
                raise ValueError("Description cannot be blank")
        return v

    account_number: str | None = Field(default=None)

    @field_validator("account_number")
    @classmethod
    def check_account_number(cls, v: str | None) -> str | None:
        if v is not None:
            if not v.startswith(("USD", "EUR", "PLN")):
                raise ValueError("Invalid account currency prefix")
        return v

    status: PaymentStatus = Field(default=PaymentStatus.PENDING)

    def is_successful(self) -> bool:
        return self.status == PaymentStatus.SUCCESS

