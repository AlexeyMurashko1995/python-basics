from pydantic import BaseModel, ConfigDict, Field, model_validator
from typing import Literal, Self
from datetime import datetime, timezone
from uuid import UUID, uuid4


class ChatMessage(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, frozen=True)
    role: Literal["system", "user", "assistant"]
    content: str = Field(min_length=1)
    token_count: int = Field(default=0, ge=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ChatSession(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
    session_id: UUID = Field(default_factory=uuid4)
    messages: list[ChatMessage] = Field(default_factory=list)
    max_tokens: int = Field(default=4096, gt=0)

    @model_validator(mode="after")
    def check_tokens_roles(self) -> Self:
        list_tokens = 0
        for message in self.messages:
            list_tokens += message.token_count
        if list_tokens > self.max_tokens:
            raise ValueError("Too many tokens")
        for i, message in enumerate(self.messages):
            if message.role == "system" and i != 0:
                raise ValueError("System role can be only at first position")
        return self
