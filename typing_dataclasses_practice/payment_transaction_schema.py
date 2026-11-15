from pydantic import BaseModel, ConfigDict, Field, model_validator
from typing import Literal, Self
from datetime import datetime, timezone


class AcquirerResponse(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, frozen=True)

    decision: Literal["approved", "declined", "error"]
    response_code: str = Field(min_length=2, max_length=2)
    auth_code: str | None = Field(default=None, min_length=6, max_length=6)
    processed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @model_validator(mode="after")
    def check_response_code(self) -> Self:
        if self.decision == "approved" and (self.response_code != "00" or self.auth_code is None):
            raise ValueError("Error")
        if (self.decision == "declined" or self.decision == "error") and (self.response_code == "00" or self.auth_code is not None):
            raise ValueError("Error 2")
        return self