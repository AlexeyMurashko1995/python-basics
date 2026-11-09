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
    amount: Decimal
    currency: Currency