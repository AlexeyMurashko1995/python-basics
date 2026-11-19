from payout_batch_schema import PayoutBatch, BatchStatus
from datetime import datetime, timezone


def submit_batch(batch: PayoutBatch) -> PayoutBatch:
    if batch.status != BatchStatus.DRAFT:
        raise ValueError("Batch status must be only draft")
    batch.status = BatchStatus.SUBMITTED
    batch.submitted_at = datetime.now(timezone.utc)
    return batch