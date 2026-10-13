import asyncio

from sqlalchemy import ForeignKey, Float, Integer, String, desc, select, func
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)
async_session = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    country: Mapped[str] = mapped_column(String(10))

    transactions: Mapped[list["Transaction"]] = relationship(back_populates="user")


class Merchant(Base):
    __tablename__ = "merchants"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    category: Mapped[str] = mapped_column(String(30))  # 'Groceries', 'Subscriptions', 'Fitness'

    transactions: Mapped[list["Transaction"]] = relationship(back_populates="merchant")


class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    merchant_id: Mapped[int] = mapped_column(ForeignKey("merchants.id"))
    amount: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(20))  # 'completed', 'failed', 'pending'

    user: Mapped["User"] = relationship(back_populates="transactions")
    merchant: Mapped["Merchant"] = relationship(back_populates="transactions")


async def seed_data(session: AsyncSession):

    u1 = User(name="Alice", country="PL")
    u2 = User(name="Bob", country="PL")
    u3 = User(name="Charlie", country="DE")

    m1 = Merchant(name="Żabka", category="Groceries")
    m2 = Merchant(name="Biedronka", category="Groceries")
    m3 = Merchant(name="Zdrofit", category="Fitness")
    m4 = Merchant(name="Spotify", category="Subscriptions")

    t1 = Transaction(user=u1, merchant=m1, amount=45.0, status="completed")
    t2 = Transaction(user=u1, merchant=m3, amount=150.0, status="completed")
    t3 = Transaction(user=u2, merchant=m2, amount=210.0, status="completed")
    t4 = Transaction(user=u2, merchant=m4, amount=20.0, status="failed")
    t5 = Transaction(user=u3, merchant=m1, amount=120.0, status="completed")
    t6 = Transaction(user=u3, merchant=m3, amount=300.0, status="completed")
    t7 = Transaction(user=u1, merchant=m2, amount=80.0, status="failed")

    session.add_all([u1, u2, u3, m1, m2, m3, m4, t1, t2, t3, t4, t5, t6, t7])
    await session.commit()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        await seed_data(session)

        query = select(Transaction.id).where(Transaction.status=="failed")

        result = await session.execute(query)
        rows = result.all()

        print("\n=== Result ===")
        for row in rows:
            print(row)
        print("===========================\n")


if __name__ == "__main__":
    asyncio.run(main())