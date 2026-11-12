from decimal import Decimal
from enum import StrEnum
from pydantic import BaseModel, Field, field_validator
from uuid import UUID, uuid4


class Currency(StrEnum):
    USD = "USD"
    EUR = "EUR"
    PLN = "PLN"


class TransferStatus(StrEnum):
    CREATED = "CREATED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"


class MoneyTransfer(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    amount: Decimal = Field(gt=0)
    currency: Currency
    recipient_iban: str = Field(min_length=15, max_length=34)
    reference: str | None = Field(default=None, max_length=140)
    status: TransferStatus = Field(default=TransferStatus.CREATED)

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