from enum import StrEnum
from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class AIModel(StrEnum):
    GPT_40 = "gpt-4o"
    CLAUDE = "claude-3-5-sonnet"
    GEMINI = "gemini-2.5-pro"


class TaskPriority(StrEnum):
    LOW = "LOW"
    NORMAL = "NORMAL"
    HIGH = "HIGH"


class ClientMetadata(BaseModel):
    client_id: UUID = Field(default_factory=uuid4)
    project_name: str = Field(min_length=3, max_length=50)