from pydantic import BaseModel, ConfigDict, Field, model_validator, computed_field, ValidationError
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

    @computed_field
    @property
    def total_tokens(self) -> int:
        total_count = 0
        for message in self.messages:
            total_count += message.token_count
        return total_count


if __name__ == "__main__":
    valid_message_1 = ChatMessage(role="system", content="user")
    valid_message_2 = ChatMessage(role="user", content="fun")
    valid_session = ChatSession(messages=[valid_message_1, valid_message_2])

    valid_session_to_dict = valid_session.model_dump()
    valid_session_to_json = valid_session.model_dump_json()

    print(valid_session_to_dict)
    print(valid_session_to_json)

    try:
        invalid_message_1 = ChatMessage(role="system", content="test")
        invalid_message_2 = ChatMessage(role="system", content="test2")
        invalid_session = ChatSession(messages=[invalid_message_1, invalid_message_2])

    except ValidationError as err:
        print(f"Error: {err}")

    try:
        invalid_message_3 = ChatMessage(role="system", content="fun")
        invalid_message_4 = ChatMessage(role="user", content="test")
        invalid_session_2 = ChatSession(messages=[invalid_message_3, invalid_message_4], description="test")

    except ValidationError as err:
        print(f"Error: {err}")
