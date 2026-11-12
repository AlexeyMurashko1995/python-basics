from decimal import Decimal
from enum import StrEnum
from pydantic import BaseModel, Field, field_validator, model_validator
from uuid import UUID, uuid4
from typing import Self


class Currency(StrEnum):
    USD = "USD"
    EUR = "EUR"
    PLN = "PLN"


class TransferStatus(StrEnum):
    CREATED = "CREATED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"


class Sender(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    company_name: str = Field(min_length=2, max_length=100)
    tax_id: str = Field(min_length=8, max_length=15)

    @field_validator("company_name")
    @classmethod
    def check_company_name(cls, v: str) -> str:
        if len(v.strip()) == 0:
            raise ValueError("Company name cannot be empty")
        return v


class MoneyTransfer(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    amount: Decimal = Field(gt=0)
    currency: Currency
    recipient_iban: str = Field(min_length=15, max_length=34)
    reference: str | None = Field(default=None, max_length=140)
    status: TransferStatus = Field(default=TransferStatus.CREATED)
    sender: Sender

    @field_validator("recipient_iban")
    @classmethod
    def check_recipient_iban(cls, v: str) -> str:
        if not (v[0:2].isalpha() and v.isascii() and v.isalnum() and v.isupper()):
            raise ValueError("Invalid recipient IBAN format")
        return v

    @field_validator("reference")
    @classmethod
    def check_reference(cls, v: str | None) -> str | None:
        if v is not None:
            if len(v.strip()) == 0:
                raise ValueError("Reference cannot be empty")
        return v

    @model_validator(mode="after")
    def check_money_transfer(self) -> Self:
        if self.currency == Currency.PLN and self.recipient_iban[0:2] != "PL":
            raise ValueError("IBAN must start with PL")
        if self.amount > Decimal("10000"):
            if self.reference is None:
                raise ValueError("Reference cannot be empty")
        return self