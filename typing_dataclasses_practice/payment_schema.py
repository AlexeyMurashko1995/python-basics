from enum import StrEnum
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from decimal import Decimal


class Currency(StrEnum):
    USD = "USD"
    EUR = "EUR"
    PLN = "PLN"


class Payment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    amount: Decimal = Field(gt=Decimal("0"))
    currency: Currency
    description: str | None = Field(default=None, max_length=100)