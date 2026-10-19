import asyncio

from sqlalchemy import Float, ForeignKey, String, func, select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class Merchant(Base):
    __tablename__ = "merchants"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    country: Mapped[str] = mapped_column(String(10), default="PL")

    payments: Mapped[list["Payment"]] = relationship(back_populates="merchant")


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True)
    merchant_id: Mapped[int] = mapped_column(ForeignKey("merchants.id"))
    amount: Mapped[float] = mapped_column(Float)
    currency: Mapped[str] = mapped_column(String(3), default="EUR")
    payment_type: Mapped[str] = mapped_column(String(20), default="deposit")  # 'deposit', 'withdrawal'
    status: Mapped[str] = mapped_column(String(20))  # 'completed', 'failed', 'pending'

    merchant: Mapped["Merchant"] = relationship(back_populates="payments")


async def seed_data(session: AsyncSession):
    m1 = Merchant(name="Intel Store", country="PL")
    m2 = Merchant(name="X2Bike", country="PL")
    m3 = Merchant(name="Coffee Hub", country="DE")

    p1 = Payment(merchant=m1, amount=45.0, payment_type="deposit", status="completed")
    p2 = Payment(merchant=m1, amount=150.0, payment_type="deposit", status="completed")
    p3 = Payment(merchant=m2, amount=210.0, payment_type="withdrawal", status="completed")
    p4 = Payment(merchant=m2, amount=20.0, payment_type="deposit", status="failed")
    p5 = Payment(merchant=m3, amount=120.0, payment_type="deposit", status="completed")
    p6 = Payment(merchant=m3, amount=300.0, payment_type="withdrawal", status="completed")
    p7 = Payment(merchant=m1, amount=80.0, payment_type="deposit", status="failed")

    session.add_all([m1, m2, m3, p1, p2, p3, p4, p5, p6, p7])
    await session.commit()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        await seed_data(session)

        query = select(Payment.id, Payment.amount, Payment.currency).where(Payment.payment_type=="deposit", Payment.amount >= 100)

        result = await session.execute(query)
        rows = result.all()

        print("\n=== Result ===")
        for row in rows:
            print(row)
        print("===========================\n")


if __name__ == "__main__":
    asyncio.run(main())