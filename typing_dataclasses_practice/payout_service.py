from payout_batch_schema import PayoutBatch, BatchStatus
from datetime import datetime, timezone


def submit_batch(batch: PayoutBatch) -> PayoutBatch:
    if batch.status != BatchStatus.DRAFT:
        raise ValueError("Batch status must be only draft")
    batch.status = BatchStatus.SUBMITTED
    batch.submitted_at = datetime.now(timezone.utc)
    return batch


def complete_batch(batch: PayoutBatch, is_settled: bool) -> PayoutBatch:
    if batch.status != BatchStatus.SUBMITTED:
        raise ValueError("Batch status must be only submitted")
    if is_settled:
        batch.status = BatchStatus.SETTLED
    else:
        batch.status = BatchStatus.REJECTED
    return batch