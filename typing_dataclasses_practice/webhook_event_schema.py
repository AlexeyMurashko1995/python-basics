from pydantic import BaseModel, ConfigDict, Field
from uuid import UUID, uuid4
from typing import Literal
from datetime import datetime, timezone


class WebhookEvent(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True, frozen=True)

    event_id: UUID = Field(default_factory=uuid4)
    event_type: Literal["payment.succeeded", "payment.failed", "refund.processed"]
    status: Literal["pending", "delivered", "failed"] = Field(default="pending")
    retry_count: int = Field(ge=0, default=0)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))