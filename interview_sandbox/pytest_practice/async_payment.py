async def get_status(payment_id: int) -> bool:
    return True


async def get_payment_confirmation(payment_id: int) -> bool:
    status = await get_status(payment_id)
    if not status:
        raise ValueError("Payment not confirmed")
    return True