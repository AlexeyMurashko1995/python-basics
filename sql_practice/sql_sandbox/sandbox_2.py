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
    country: Mapped[str] = mapped_column(String(10))

    payments: Mapped[list["Payment"]] = relationship(back_populates="merchant")


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True)
    merchant_id: Mapped[int] = mapped_column(ForeignKey("merchants.id"))
    amount: Mapped[float] = mapped_column(Float)
    currency: Mapped[str] = mapped_column(String(3), default="EUR")
    status: Mapped[str] = mapped_column(String(20))  # 'completed', 'failed', 'pending'

    merchant: Mapped["Merchant"] = relationship(back_populates="payments")


async def seed_data(session: AsyncSession):
    m1 = Merchant(name="Intel Store", country="PL")
    m2 = Merchant(name="X2Bike", country="PL")
    m3 = Merchant(name="Coffee Hub", country="DE")

    p1 = Payment(merchant=m1, amount=45.0, status="completed")
    p2 = Payment(merchant=m1, amount=150.0, status="completed")
    p3 = Payment(merchant=m2, amount=210.0, status="completed")
    p4 = Payment(merchant=m2, amount=20.0, status="failed")
    p5 = Payment(merchant=m3, amount=120.0, status="completed")
    p6 = Payment(merchant=m3, amount=300.0, status="completed")
    p7 = Payment(merchant=m1, amount=80.0, status="failed")

    session.add_all([m1, m2, m3, p1, p2, p3, p4, p5, p6, p7])
    await session.commit()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        await seed_data(session)


        # query = select(Payment.id).where(Payment.status=="completed", Payment.amount > 100)
        # query = select(func.count(Payment.id), func.sum(Payment.amount)).where(Payment.status=="completed")
        query = select(Merchant.name, func.sum(Payment.amount)).join(Payment).where(Payment.status=="completed").group_by(Merchant.name)

        result = await session.execute(query)
        rows = result.all()

        print("\n=== Result ===")
        for row in rows:
            print(row)
        print("===========================\n")


if __name__ == "__main__":
    asyncio.run(main())