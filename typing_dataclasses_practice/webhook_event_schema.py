from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator
from uuid import UUID, uuid4
from typing import Literal
from datetime import datetime, timezone
from typing import Self


class WebhookEvent(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, frozen=True)

    event_id: UUID = Field(default_factory=uuid4)
    event_type: Literal["payment.succeeded", "payment.failed", "refund.processed"]
    status: Literal["pending", "delivered", "failed"] = Field(default="pending")
    retry_count: int = Field(ge=0, default=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class WebhookBatch(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    batch_id: UUID = Field(default_factory=uuid4)
    endpoint_url: str

    @field_validator("endpoint_url")
    @classmethod
    def check_endpoint_url(cls, v: str) -> str:
        if not v.startswith("https://"):
            raise ValueError("Endpoint must start with https://")
        return v

    events: list[WebhookEvent] = Field(default_factory=list)
    max_batch_size: int = Field(gt=0, default=10)

    @model_validator(mode="after")
    def check_events(self) -> Self:
        if len(self.events) > self.max_batch_size:
            raise ValueError("Too many events")
        for event in self.events:
            if event.status == "delivered":
                raise ValueError("Status cannot be delivered")
        return self