from pydantic import BaseModel, ConfigDict, Field, model_validator
from typing import Literal, Self
from datetime import datetime, timezone
from uuid import UUID, uuid4
from enum import StrEnum


class Currency(StrEnum):
    USD = "USD"
    EUR = "EUR"
    PLN = "PLN"


class AcquirerResponse(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, frozen=True)

    decision: Literal["approved", "declined", "error"]
    response_code: str = Field(min_length=2, max_length=2)
    auth_code: str | None = Field(default=None, min_length=6, max_length=6)
    processed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @model_validator(mode="after")
    def check_response_code(self) -> Self:
        if self.auth_code is not None and not self.auth_code.isdigit():
            raise ValueError("Auth code must contain only digits")
        if self.decision == "approved" and (self.response_code != "00" or self.auth_code is None):
            raise ValueError("Approved decision requires response code '00' and auth_code")
        if self.decision in ("declined", "error") and (self.response_code == "00" or self.auth_code is not None):
            raise ValueError("Declined or error decision cannot have response code '00' or auth_code")
        return self


class PaymentTransaction(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    transaction_id: UUID = Field(default_factory=uuid4)
    merchant_id: str = Field(min_length=1)
    amount: int = Field(gt=0)
    currency: Currency
    status: Literal["created", "authorized", "declined", "failed"] = Field(default="created")
    acquirer_response: AcquirerResponse | None = Field(default=None)

    @model_validator(mode="after")
    def check_payment_transaction(self) -> Self:
        if self.status == "created":
            if self.acquirer_response is not None:
                raise ValueError("Acquirer response must be empty for created status")
            return self

        if self.acquirer_response is None:
            raise ValueError("Acquirer response is required for processed transaction")

        if self.status == "authorized" and self.acquirer_response.decision != "approved":
            raise ValueError("Authorized transaction requires approved acquirer decision")
        if self.status == "declined" and self.acquirer_response.decision != "declined":
            raise ValueError("Declined transaction requires declined acquirer decision")
        if self.status == "failed" and self.acquirer_response.decision != "error":
            raise ValueError("Failed transaction requires error acquirer decision")

        return self
