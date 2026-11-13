from pydantic import BaseModel, ConfigDict, Field
from typing import Literal
from datetime import datetime, timezone


class ChatMessage(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, frozen=True)
    role: Literal["system", "user", "assistant"]
    content: str = Field(min_length=1)
    tokens_count: int = Field(default=0, ge=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))