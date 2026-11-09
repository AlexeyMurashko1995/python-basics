from enum import StrEnum
from pydantic import BaseModel, Field, field_validator
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

    @field_validator("description")
    @classmethod
    def check_description(cls, v: str | None) -> str | None:
        if v is not None:
            if v.strip() == "":
                raise ValueError("Description cannot be blank")
        return v
