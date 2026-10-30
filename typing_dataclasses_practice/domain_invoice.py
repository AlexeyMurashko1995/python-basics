from dataclasses import dataclass
from decimal import Decimal
from typing import Literal


@dataclass
class Invoice:
    id: str
    user_id: str
    amount: Decimal
    currency: Literal["USD", "EUR", "PLN"]
    status: Literal["draft", "issued", "paid", "cancelled"] = "draft"
    description: str | None = None