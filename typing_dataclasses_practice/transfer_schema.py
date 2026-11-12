from decimal import Decimal
from enum import StrEnum
from pydantic import BaseModel, Field
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