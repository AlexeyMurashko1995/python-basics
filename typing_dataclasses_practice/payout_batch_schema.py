from pydantic import BaseModel, Field, ConfigDict, field_validator, model_validator
from enum import StrEnum
from uuid import UUID, uuid4
from datetime import datetime, timezone
from typing import Self


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

    @field_validator("iban")
    @classmethod
    def check_iban(cls, v: str) -> str:
        cleaned_v = v.replace(" ", "").upper()
        if not (15 <= len(cleaned_v) <= 34):
            raise ValueError("IBAN must be between 15 and 34 characters")
        if not (cleaned_v.isascii() and cleaned_v.isalnum()):
            raise ValueError("IBAN must contain only ASCII letters and digits")
        if not (cleaned_v[:2].isalpha() and cleaned_v[2:4].isdigit()):
            raise ValueError("IBAN must start with 2 letters followed by 2 digits")
        return cleaned_v

    amount: int = Field(gt=0)
    fee: int = Field(ge=0, default=0)


class PayoutBatch(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    batch_id: UUID = Field(default_factory=uuid4)
    currency: PayoutCurrency
    status: BatchStatus = Field(default=BatchStatus.DRAFT)
    items: list[PayoutItem] = Field(min_length=1, max_length=100)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    submitted_at: datetime | None = None

    @model_validator(mode="after")
    def validate_batch(self) -> Self:
        seen = set()
        for item in self.items:
            if item.item_id in seen:
                raise ValueError("This item already exists")
            seen.add(item.item_id)
        if self.status == BatchStatus.DRAFT and self.submitted_at is not None:
            raise ValueError("Draft cannot have submitted time")
        elif self.status != BatchStatus.DRAFT and self.submitted_at is None:
            raise ValueError("Submitted time is necessary")
        return self
    @property
    def total_amount(self) -> int:
        return sum(item.amount for item in self.items)
    @property

    def total_fee(self) -> int:
        return sum(item.fee for item in self.items)
