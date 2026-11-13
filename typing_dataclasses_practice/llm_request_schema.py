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


class LLMRequest(BaseModel):
    request_id: UUID = Field(default_factory=uuid4)
    model: AIModel
    prompt: str = Field(min_length=1, max_length=10000)
    system_prompt: str | None = Field(default=None, max_length=2000)
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    max_tokens: int = Field(default=1024, gt=0, le=16384)
    priority: TaskPriority = Field(default=TaskPriority.NORMAL)
    client: ClientMetadata
