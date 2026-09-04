from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from pydantic import BaseModel

app = FastAPI()

engine = create_async_engine("sqlite+aiosqlite:///:memory:")

async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db():
    async with async_session_factory() as session:
        print("Session opened")
        yield session
        print("Session closed")


class PaymentCreate(BaseModel):
    account_id: int
    amount: float


async def process_amount(account_id: int, amount: float, session: AsyncSession):
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if account_id == 999:
        raise PermissionError("Account is blocked")
    return f"Payment of {amount} for account {account_id} processed"


@app.post("/payments")
async def create_payment(payload: PaymentCreate, session: AsyncSession = Depends(get_db)):
    try:
        new_payment = await process_amount(account_id=payload.account_id, amount=payload.amount, session=session)
        return {"status": "success", "details": new_payment}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))

