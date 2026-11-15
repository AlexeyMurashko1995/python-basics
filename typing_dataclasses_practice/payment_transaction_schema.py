from pydantic import BaseModel, ConfigDict, Field
from typing import Literal
from datetime import datetime, timezone


class AcquirerResponse(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, frozen=True)

    decision: Literal["approved", "declined", "error"]
    response_code: str = Field(min_length=2, max_length=2)
    auth_code: str | None = Field(default=None, min_length=6, max_length=6)
    processed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))