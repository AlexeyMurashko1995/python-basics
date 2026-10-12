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


class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    amount: Mapped[float] = mapped_column(Float)
    status: Mapped[str] = mapped_column(String(20))  # 'completed', 'failed', 'pending'

    user: Mapped["User"] = relationship(back_populates="transactions")


async def seed_data(session: AsyncSession):
    u1 = User(name="Alice", country="PL")
    u2 = User(name="Bob", country="PL")
    u3 = User(name="Charlie", country="DE")

    t1 = Transaction(user=u1, amount=100.0, status="completed")
    t2 = Transaction(user=u1, amount=250.0, status="failed")
    t3 = Transaction(user=u2, amount=500.0, status="completed")
    t4 = Transaction(user=u2, amount=50.0, status="completed")
    t5 = Transaction(user=u3, amount=1200.0, status="failed")
    t6 = Transaction(user=u3, amount=300.0, status="completed")

    session.add_all([u1, u2, u3, t1, t2, t3, t4, t5, t6])
    await session.commit()


async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        await seed_data(session)

        # query = select(Transaction.id, Transaction.amount).where(Transaction.status == "failed")
        # query = select(Transaction.user_id, Transaction.amount).where(Transaction.amount > 200).order_by(desc(Transaction.amount))
        # query = select(func.sum(Transaction.amount)).where(Transaction.status == "completed")
        query = select(User.name).where(User.country == "PL")

        result = await session.execute(query)
        rows = result.all()

        print("\n=== Result ===")
        for row in rows:
            print(row)
        print("===========================\n")


if __name__ == "__main__":
    asyncio.run(main())