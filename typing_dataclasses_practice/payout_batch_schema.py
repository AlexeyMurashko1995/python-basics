from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum
from uuid import UUID, uuid4


class PayoutCurrency(StrEnum):
    USD = "USD"
    EUR = "EUR"
    PLN = "PLN"


class BatchStatus(StrEnum):
    DRAFT = "draft"
    SUBMITTED = "submitted"
    SETTLED = "settled"
    REJECTED = "rejected"


class PayoutItem(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, frozen=True)

    item_id: UUID = Field(default_factory=uuid4)
    merchant_id: str = Field(min_length=1)
    iban: str
    amount: int = Field(gt=0)
    fee: int = Field(ge=0, default=0)